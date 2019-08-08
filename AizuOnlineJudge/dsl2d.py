# AOJ DSL_2_D
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_D

INF = (-1, 2**31 - 1)
line = input()
n, q = list(map(int, line.split()))
N = 1
while N < n + 1:
    N *= 2
a = [INF for _ in range(0, 2 * N - 1)]

def find(i, k, l, r):
    z = a[0]
    while True:
        m = (l + r) // 2
        if i < m:
            k = k * 2 + 1
            r = m
        else:
            k = k * 2 + 2
            l = m
        z = max(z, a[k])
        if k >= N - 1:
            break
    return z[1]

def update(s, t, x, k, l, r):
    if r <= s or t <= l:
        return
    elif s <= l and r <= t:
        a[k] = x
        return
    m = (l + r) // 2
    update(s, t, x, k * 2 + 1, l, m)
    update(s, t, x, k * 2 + 2, m, r)
    return

for t in range(0, q):
    line = input()
    qu = list(map(int, line.split()))
    if qu[0] == 0:
        update(qu[1], qu[2]+1, (t, qu[3]), 0, 0, N)
    elif qu[0] == 1:
        ans = find(qu[1], 0, 0, N)
        print(ans)