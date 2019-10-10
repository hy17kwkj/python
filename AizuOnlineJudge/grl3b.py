# AOJ GRL_3_B
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_B

import sys

sys.setrecursionlimit(100000)

V, E = list(map(int, input().split()))
Edge = [list(map(int, input().split())) for _ in range(0, E)]

ord = [0 for _ in range(0, V)]
low = [0 for _ in range(0, V)]
used = [False for _ in range(0, V)]
bridge = []

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
        # 後退辺か
        elif t != p:
            # ord[t]の最小値
            low[s] = min(low[s], ord[t])

for s in range(0, V):
    if used[s] == False:
        dfs(s, -1, 0)

for s, t in Edge:
    if ord[s] < low[t] or ord[t] < low[s]:
        if s < t:
            bridge += [(s, t)]
        else:
            bridge += [(t, s)]

bridge.sort()
for s, t in bridge:
    print(s, t)