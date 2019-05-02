# AOJ 1106
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1106

import sys
import math

def gcd(a, b):
    if a < b:
        a, b = b, a
    r = b
    while r != 0:
        r = a % b
        if r == 0:
            return b
        a, b = b, r

def factor(a, b, c):
    disc = b * b - 4 * a * c
    if disc < 0:
        print("Impossible")
        return
    rd = math.sqrt(disc)
    if rd - math.floor(rd) > 0:
        print("Impossible")
        return
    aa = 1
    p = 2 * a
    q = b - rd
    if q == 0:
        p = 1
    else:
        d = gcd(p, q)
        p /= d
        q /= d

    r = 2 * a
    s = (b + rd) #* (a / aa)
    if s == 0:
        r = 1
    else:
        d = gcd(r, s)
        r /= d
        s /= d
    if p < 0:
        p, q = -p, -q
    if r < 0:
        r, s = -r, -s
    if p < r or (p == r and q < s):
        p, q, r, s = r, s, p, q
    print("%d %d %d %d" % (p, q, r, s))
    return

"""
while True:
    line = input().split()
    a, b, c = map(int, list(line))
    if a == 0 and b == 0 and c == 0:
        break
    factor(a, b, c)
"""

factor(16, -376, 2193)
