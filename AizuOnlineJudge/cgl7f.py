# AOJ CGL_7_F
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_7_F

import math

line = input()
px, py = list(map(int, line.split()))
line = input()
cx, cy, r = list(map(int, line.split()))

def solve():
    d2 = (px - cx)*(px - cx) + (py - cy)*(py - cy)
    d = math.sqrt(d2)
    sine = r / d
    sin2 = r * r / d2
    cosine = math.sqrt(1 - sin2)
    cos2 = 1 - sin2
    x1 = (cx - px) * cos2 - (cy - py) * sine * cosine + px
    y1 = (cx - px) * sine * cosine + (cy - py) * cos2 + py
    x2 = (cx - px) * cos2 + (cy - py) * sine * cosine + px
    y2 = - (cx - px) * sine * cosine + (cy - py) * cos2 + py
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    print(x1, y1)
    print(x2, y2)

solve()
