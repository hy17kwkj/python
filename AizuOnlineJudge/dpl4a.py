# AOJ DPL_4_A
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_4_A

coins = []
f = open("python\input_dpl4a.txt")
line = f.readline()
#line = input()
n, v = list(map(int, line.split()))
for _ in range(0, 4):
    line = f.readline()
    #line = input()
    c = list(map(int, line.split()))
    coins += [c]

def solve(n, v):
    ab = {}
    for i in range(0, n):
        for j in range(0, n):
            a = coins[0][i] + coins[1][j]
            if a not in ab:
                ab[a] = 1
            else:
                ab[a] += 1
    cd = {}
    low = 10 ** 17
    high = 0
    for i in range(0, n):
        for j in range(0, n):
            a = coins[2][i] + coins[3][j]
            if a not in cd:
                cd[a] = 1
                low = min(low, a)
                high = max(high, a)
            else:
                cd[a] += 1
    ans = 0
    for k in ab:
        if v - k < low or high < v - k:
            continue
        if v - k in cd:
            ans += ab[k] * cd[v - k]
    return ans

print(solve(n, v))
