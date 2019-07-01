# AOJ NTL_1_E
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_E

import math

def Euclid(a, b):
    if a == 0 and b > 0:
        return 0, 1
    r = q = 0
    x = y = 0
    if a >= b:
        r = a % b
        q = a // b
        x1, y1 = Euclid(r, b)
        x = x1
        y = y1 - q * x1
    else:
        r = b % a
        q = b // a
        x1, y1 = Euclid(r, a)
        x = y1 - q * x1
        y = x1
    return x, y

line = input()
a, b = list(map(int, line.split()))
x, y = Euclid(a, b)
if x > y:
    t = math.floor(- (x - y)/(a + b))
    x1 = b * t + x
    y1 = - a * t + y
    if abs(x) + abs(y) >= abs(x1) + abs(y1):
        x, y = x1, y1
print(x, y)
