# AOJ DSL_1_A
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A

import sys

line = input()
n, q = list(map(int, line.split()))
rel = {}
for i in range(0, n):
    rel[i] = []
parent = [i for i in range(0, n)]

def find(x):
    if parent[x] == x:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y

def unite(x, y):
    rx = find(x)
    ry = find(y)
    if rx < ry:
        parent[ry] = rx
    else:
        parent[rx] = ry

def same(x, y):
    return find(x) == find(y)

for _ in range(0, q):
    line = input()
    query, x, y = list(map(int, line.split()))
    if query == 0:
        unite(x, y)
    elif query == 1:
        print(1 if same(x, y) else 0)
