# AOJ DPL_2_A
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_2_A

import copy

edge = []
dp = []
INF = 1000000000

def tsp(v, e, dp):
    dp1 = [ [INF] * v for _ in range(0, v)]
    print(dp)
    for i in range(0, v + 1):
        for s, t, d in edge:
            for j in range(0, v):
                if dp[j][s] + d > 0:
                    dp1[s][t] = min(dp[j][s] + d, dp1[s][t])
        print(dp1)
        dp = copy.deepcopy(dp1)
        dp1 = [ [INF] * v for _ in range(0, v)]
        print(dp)


f = open("python\input_dpl2a.txt")
#f = open("python\in11.txt")
line = f.readline()
#line = input()
v, e = list(map(int, line.split()))
dp = [ [INF] * v for _ in range(0, 1 << v)]
for _ in range(0, e):
    line = f.readline()
    #line = input()
    s, t, d = list(map(int, line.split()))
    dp[1 << s]
tsp(v, e, dp)
print(dp)