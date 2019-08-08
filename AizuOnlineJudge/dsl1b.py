# AOJ DSL_1_B
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_B

line = input()
n, q = list(map(int, line.split()))
rel = {}
for i in range(0, n):
    rel[i] = []
parent = [i for i in range(0, n)]
rank = [0] * n
weight = [0] * n

def find(x):
    if parent[x] == x:
        return x
    else:
        y = find(parent[x])
        weight[x] += weight[parent[x]]
        parent[x] = y
        return y

def union(x, y, w):
    rx = find(x)
    ry = find(y)
    if rank[rx] < rank[ry]:
        parent[rx] = ry
        weight[rx] = w - weight[x] + weight[y]
    else:
        parent[ry] = rx
        weight[ry] = - w - weight[y] + weight[x]
        if rank[rx] == rank[ry]:
            rank[rx] += 1

def same(x, y):
    return find(x) == find(y)

def diff(x, y):
    return weight[x] - weight[y]

for _ in range(0, q):
    line = input()
    query = list(map(int, line.split()))
    if query[0] == 0:
        x, y, z = query[1:]
        union(x, y, z)
    elif query[0] == 1:
        x, y = query[1:]
        if same(x, y):
            print(diff(x, y))
        else:
            print("?")
