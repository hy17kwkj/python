# AOJ NTL_1_C
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_C

import functools 

def gcd(a, b):
    if a > 0 and b == 0:
        return a
    if a < b:
        a, b = b, a
    r = a % b
    return gcd(b, r)

def lcm(a, b):
    return  a * b // gcd(a, b)

line = input()
n = int(line)
line = input()
a = list(map(int, line.split()))
print(functools.reduce(lambda x,y: lcm(x, y), a))
