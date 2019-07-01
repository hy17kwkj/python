# DPL_1_A
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_A

import sys
sys.setrecursionlimit(10000)

dp = []
coins = []
INF = 9999999

def change(n, m):
    if n == 0:
        return 0
    if dp[n] == INF:
        res = INF
        for j in range(0, m):
            if n - coins[j] >= 0:
                res = min(res, change(n - coins[j], m) + 1)
        dp[n] = res
    return dp[n]

f = open("python\input_dpl1a.txt")
#f = open("python\in11.txt")
line = f.readline()
#line = input()
n, m = list(map(int, line.split()))
line = f.readline()
#line = input()
d = list(map(int, line.split()))
coins = sorted(d)
coins.reverse()
dp = [INF] * (n + 1)
change(n, m)
print(dp[n])
