# AOJ DPL_4_B
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_4_B

import bisect 
from itertools import combinations

coins = []
line = input()
n, k, l, r = list(map(int, line.split()))
line = input()
coins = list(map(int, line.split()))

popcount = [bin(a).count('1') for a in range(0, 1024)]

def solve():
    n2 = n // 2
    c1 = [ list(map(sum, combinations(coins[:n2], z))) for z in range(0, n2 + 1) ]
    c2 = [ list(map(sum, combinations(coins[n2:], z))) for z in range(0, n - n2 + 1) ]
    for i in range(0, n - n2 + 1):
        c2[i].sort()
    ans = 0
    for i in range(0, k + 1):
        print(i)
        if k - i < 0 or k - i > n - n2 or i > n2:
            continue
        for a in c1[i]:
            low = bisect.bisect_left(c2[k - i], l - a)
            high = bisect.bisect_right(c2[k - i], r - a)
            ans += high - low
    return ans

print(solve())
