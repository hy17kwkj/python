# AOJ GRL_2_B
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_B

import sys
from heapq import heappush, heappop

V, E, r = list(map(int, input().split()))
Edge = [list(map(int, input().split())) for _ in range(0, E)]

# Chu-Liu/Edmonds のアルゴリズム
def solve(V, Edge, r):
    if V <= 1:
        return 0

    # 各頂点に入る最小コストの辺を選んでMとする。
    q = [[] for _ in range(0, V)]
    for s, t, w in Edge:
        heappush(q[t], (w, s))
    M = [(0, -1) for _ in range(0, V)]
    for t in range(0, V):
        if t != r:
            w, s = heappop(q[t])
            M[t] = (w, s)

    """
    1 <- 2 <- 3 <- 1 <- 4  impossible
    4 <- 1 <- 2 <- 3 <- 1
    """
    # Mから閉路を検出する。
    used = [False for _ in range(0, V)]
    hist = []
    cycle = []
    for t in range(0, V):
        w, s = M[t]

        # 出発点もしくは使用済みなら次の頂点へ
        if s == -1 or used[t] == True:
            continue
        if used[t] == False:
            used[t] = True
            # たどった頂点をhistに格納する。
            hist += [t]
            tt = s
            # 使用済みでない頂点を辺の向きの逆順にたどる
            while used[tt] == False:
                used[tt] = True
                hist += [tt]
                w, s = M[tt]
                # 出発点に戻ってきたらhistを空にしてループを抜ける
                if s == -1:
                    hist = []
                    break
                tt = s
            # 使用済みの点に戻る かつ 出発点に戻っていない かつ histが1個以上ある
            if used[tt] == True and s != -1 and 0 < len(hist):
                try:
                    # いま見ている頂点ttをすでにたどっているか？
                    k = hist.index(tt)
                    cycle = hist[k:]
                except:
                    # たどっていなければ閉路ではないので次の頂点へ
                    continue
                finally:
                    pass
                # たどっているので閉路があった。ループを抜ける。
                break

    # 閉路がなければ有向最小全域木が求められている。
    if len(cycle) == 0:
        # Mに含まれる辺のコストの総和が解となる。
        return sum(m[0] for m in M)

    # 閉路の頂点番号の最小値を代表にして、グラフを縮約する。
    parent = min(cycle)
    # 縮約後につけ直した頂点番号
    rn = [0 for _ in range(0, V)]
    # 頂点番号の付け直し処理
    k = 0
    for t in range(0, V):
        if k == parent:
            k += 1
        if t in cycle:
            rn[t] = parent
        else:
            rn[t] = k
            k += 1

    # 縮約したグラフ(Vp, Ep, r)を作る。
    Vp = V - len(cycle) + 1
    Ep = []
    for s, t, w in Edge:
        if s in cycle:
            if t in cycle:
                continue
            else:
                Ep += [[parent, rn[t], w]]
        else:
            if t in cycle:
                Ep += [[rn[s], parent, w - M[t][0]]]
            else:
                Ep += [[rn[s], rn[t], w]]

    # 出発点の番号もつけ直す
    r = rn[r]
    # 縮約したグラフに再帰的に呼び出した返り値と、閉路のコストの和が解となる。
    return solve(Vp, Ep, r) + sum(M[t][0] for t in cycle)

print(solve(V, Edge, r))
