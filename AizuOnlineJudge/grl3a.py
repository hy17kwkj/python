# AOJ GRL_3_A
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_A

import sys

sys.setrecursionlimit(100000)

V, E = list(map(int, input().split()))
Edge = [list(map(int, input().split())) for _ in range(0, E)]

ord = [0 for _ in range(0, V)]
low = [0 for _ in range(0, V)]
used = [False for _ in range(0, V)]
articulation = []

G = [ [] for _ in range(0, V)]
for s, t in Edge:
    G[s] += [t]
    G[t] += [s]

# pは親となる頂点
def dfs(s, p, k):
    global articulation
    used[s] = True
    ord[s] = k
    low[s] = ord[s]
    k += 1
    c = 0

    # sから始まる辺
    for t in G[s]:
        # まだ探索していないか
        if used[t] == False:
            c += 1
            dfs(t, s, k)
            # DFSの葉の方向進める頂点のlowlinkの最小値
            low[s] = min(low[s], low[t])
            # 始点ではなく、ord[s] <= low[t] となる頂点ｔがあればそれが関節点
            if p != -1 and ord[s] <= low[t]:
                articulation += [s]
        # 後退辺か
        elif t != p:
            # ord[t]の最小値
            low[s] = min(low[s], ord[t])

    # 始点のとき
    if p == -1 and c >= 2:
        articulation += [s]

for s in range(0, V):
    if used[s] == False:
        dfs(s, -1, 0)

answer = list(set(articulation))
answer.sort()
if len(articulation) > 0:
    print("\n".join(list(map(str, answer))))
