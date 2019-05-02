# 10000以下の素数を表示する。

import math

def sieve(n):
    rt = math.floor(math.sqrt(n))
    si = [0] * (n+1)
    si[0] = si[1] = 1
    for i in range(2, rt):
        if si[i] == 1:
            continue
        j = i * 2
        while j <= n:
            si[j] = 1
            j += i
    for i in range(0, n+1):
        if si[i] != 1:
            print(i, end=" ")

sieve(10000)
