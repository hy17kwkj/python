# AOJ DSL_2_B
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_B

line = input()
n, q = list(map(int, line.split()))
N = 1
while N < n + 1:
    N *= 2
a = [0 for _ in range(0, 2 * N - 1)]

def update(k, v):
    k += N - 1
    a[k] += v
    while k > 0:
        k = (k - 1) // 2
        a[k] = a[k * 2 + 1] + a[k * 2 + 2]

def query(x, y, k, l, r):
    if r <= x or y <= l:
        return 0
    elif x <= l and r <= y:
        return a[k]
    m = (l + r) // 2
    return query(x, y, k * 2 + 1, l, m) + query(x, y, k * 2 + 2, m, r)

for _ in range(0, q):
    line = input()
    c, x, y = list(map(int, line.split()))
    if c == 0:
        update(x, y)
    elif c == 1:
        ans = query(x, y + 1, 0, 0, N)
        print(ans)
