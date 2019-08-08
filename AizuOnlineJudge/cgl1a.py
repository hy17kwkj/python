# AOJ CGL_1_A
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_1_A

import math

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
        xx = x1 + dx * ip / l1
        yy = y1 + dy * ip / l1
        print(xx, yy)

solve()
