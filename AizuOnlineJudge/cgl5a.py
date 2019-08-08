# AOJ CGL_5_a
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_5_A

import math
from itertools import combinations
from operator import itemgetter

pts = []
line = input()
n = int(line)
for _ in range(0, n):
    line = input()
    x, y = list(map(float, line.split()))
    pts += [[x, y]]

def dist(p, q):
    x1, y1 = p
    x2, y2 = q
    return (x1 - x2)**2 + (y1 - y2)**2

def solve(p, axis):
    print(p)
    n = len(p)
    if n <= 3:
        d = 100000
        q1 = q2 = []
        for p1, p2 in list(combinations(p, 2)):
            d = min(d, dist(p1, p2))
        return d

    mid = n // 2
    px, py = zip(*p)
    axis1 = 2 * len(set(px)) <= n
    axis2 = not axis1
    if axis1 != axis:
        p.sort(key = itemgetter(axis1))

    xy0 = p[mid][axis1]
    left = p[:mid]
    right = p[mid:]
    d = min(solve(left, axis1), solve(right, axis1))
    rd = math.sqrt(d)

    Q = []
    for pp in left[::-1]:
        if pp[axis1] < xy0 - rd:
            break
        Q.append(pp)
    for pp in right:
        if pp[axis1] > xy0 + rd:
            break
        Q.append(pp)
    Q.sort(key = itemgetter(axis2))
    for i, p1 in enumerate(Q):
        dd = p1[axis2] + rd
        for p2 in Q[i + 1:]:
            if p2[axis2] > dd:
                break
            norm = dist(p1, p2)
            if d > norm:
                d = norm
    return d

pts.sort(key = itemgetter(0))
ans = solve(pts, 0)
print('%.16f' % math.sqrt(ans))
