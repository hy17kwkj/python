# AOJ GRL_1_C
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C

INF = 999999999999

def BellmanFord_edge(s, v, edge):
    dp = [INF] * v
    dp[s] = 0
    for i in range(0, v):
        dp1 = dp[:]
        for fr, to, d in edge:
            if dp[fr] == INF:
                continue
            if dp[to] > dp[fr] + d:
                dp[to] = dp[fr] + d
                if i == v - 1:
                    return -1
        if dp == dp1:
            break
    return dp

f = open("python\input_grl1c.txt")
dp = []
line = f.readline()
#line = input()
v, e = list(map(int, line.split()))
edge = []
for _ in range(0, e):
    line = f.readline()
    #line = input()
    s, t, d = list(map(int, line.split()))
    edge += [[s, t, d]]
for s in range(0, v):
    dp = BellmanFord_edge(s, v, edge)
    if dp == -1:
        print("NEGATIVE CYCLE")
        break
    else:
        print(" ".join(map(str, [dp[t] if dp[t] != INF else "INF" for t in range(0, v)])))
