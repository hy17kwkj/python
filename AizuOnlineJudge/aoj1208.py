# AOJ 1208
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1208

import sys
import math

def rational(p, n):
    rt = math.sqrt(p)
    k = math.floor(rt)
    mi = n
    mx = n
    mikk = 0
    mibb = 0
    mxkk = 0
    mxbb = 0
    for i in range(1, n+1):
        a = (rt - k) * i
        b = math.floor(a)
        if mi > a - b and k * i + b <= n:
            mi = a - b
            mikk = i
            mibb = b
        if mx > b + 1 - a and k * i + (b + 1) <= n:
            mx = b + 1 - a
            mxkk = i
            mxbb = b
    print("{}/{} {}/{}".format(k * mikk + mibb, mikk, k * mxkk + (mxbb + 1), mxkk))

while True:
    line = input().split()
    p, n = map(int, list(line))
    if p == 0 and n == 0:
        break
    rational(p, n)
