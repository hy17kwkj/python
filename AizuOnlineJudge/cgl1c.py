# AOJ CGL_1_C
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_1_C

import math

eps = 10 ** -8

line = input()
x1, y1, x2, y2 = list(map(int, line.split()))
line = input()
q = int(line)
pts = []
for _ in range(0, q):
    line = input()
    x, y = list(map(int, line.split()))
    pts += [[x, y]]

def solve():
    l1 = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    for x, y in pts:
        l2 = math.sqrt((x - x1)**2 + (y - y1)**2)
        dx = (x2 - x1) / l1
        dy = (y2 - y1) / l1
        ip = (x - x1) * (x2 - x1) + (y - y1) * (y2 - y1)
        sine = (x - x1) * (y2 - y1) - (y - y1) * (x2 - x1)
        if sine < 0.0:
            print("COUNTER_CLOCKWISE")
        elif sine > 0.0:
            print("CLOCKWISE")
        elif abs(ip - l1 * l2) < eps:
            if l1 < l2:
                print("ONLINE_FRONT")
            else:
                print("ON_SEGMENT")
        elif ip + l1 * l2 < eps:
            print("ONLINE_BACK")
solve()
