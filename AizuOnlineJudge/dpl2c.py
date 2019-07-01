# DPL_2_C
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_2_C

import math

pts = []
f = open("python\input_dpl2c.txt")
line = f.readline()
#line = input()
N = int(line)
for _ in range(0, N):
    line = f.readline()
    #line = input()
    x, y = list(map(int, line.split()))
    pts += [[x, y]]

def dist(i, j):
    x1, y1 = pts[i]
    x2, y2 = pts[j]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def btsp():
    dp = [ [0] * N for _ in range(0, N)]
    for i in range(1, N):
        dp[0][i] = dp[0][i - 1] + dist(i - 1, i)
    for i in range(1, N):
        for j in range(i, N):
            if i == j - 1 or i == j:
                m = 10 ** 10
                for k in range(0, i):
                    m = min(m, dp[k][i] + dist(j, k))
                dp[i][j] = m
            else:
                dp[i][j] = dp[i][j - 1] + dist(j - 1, j)
    print(dp)
    return dp[N - 1][N - 1]

print(btsp())