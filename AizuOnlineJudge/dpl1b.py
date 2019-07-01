# DPL_1_B
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_B

items = []
used = [] 
dp = []

def knapsack(n, e):
    for i in range(0, n + 1):
        res = 0
        for j in range(0, e):
            v, w = items[j]
            if i >= w:
                dp[j + 1][i] = max(dp[j][i - w] + v, dp[j][i])
            else:
                dp[j + 1][i] = dp[j][i]
        print(i, dp)
    return

f = open("python\input_dpl1b.txt")
#f = open("python\in11.txt")
line = f.readline()
#line = input()
E, W = list(map(int, line.split()))
for _ in range(0, E):
    line = f.readline()
    #line = input()
    v, w1 = list(map(int, line.split()))
    items += [[v, w1]]
dp = [[0] * (W + 1) for _ in range(0, E + 1)]
knapsack(W, E)
print(dp[E][W])
