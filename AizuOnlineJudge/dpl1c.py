# DPL_1_C
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_C

items = []

def knapsack(n):
    for i in range(0, n + 1):
        res = 0
        for v, w in items:
            if i >= w:
                res = max(res, dp[i - w] + v)
        dp[i] = res
    return dp[n]

line = input()
E, W = list(map(int, line.split()))
for _ in range(0, E):
    line = input()
    v, w1 = list(map(int, line.split()))
    items += [[v, w1]]
dp = [0] * (W + 1)
used = [False] * E
knapsack(W)
print(dp[W])
