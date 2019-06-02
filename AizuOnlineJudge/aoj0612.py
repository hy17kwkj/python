# AOJ 0612
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0612

castle = []
cmp = []
h = w = 0
left = 0

def initial():
    global h, w, left
    left = h * w
    for i in range(0, h):
        left -= castle[i].count(0)
    for i in range(0, h):
        c = []
        for j in range(0, w):
            if castle[i][j] == 0:
                c.append(-99)
            else:
                a  = castle[i - 1][j - 1:j + 2].count(0)
                a += castle[i][j - 1: j + 2].count(0)
                a += castle[i + 1][j - 1: j + 2].count(0)
                c.append(a)
        cmp.append(c)

def wave(xy):
    global h, w, left
    z = []
    xy1 = []
    for i, j in xy:
        if castle[i][j] > 0 and castle[i][j] <= cmp[i][j]:
            castle[i][j] = 0
            left -= 1
            z.append((i, j))
    for i, j in z:
        cmp[i - 1][j - 1] += 1
        cmp[i - 1][j    ] += 1
        cmp[i - 1][j + 1] += 1
        cmp[i    ][j - 1] += 1
        cmp[i    ][j    ] = -99
        cmp[i    ][j + 1] += 1
        cmp[i + 1][j - 1] += 1
        cmp[i + 1][j    ] += 1
        cmp[i + 1][j + 1] += 1
        y = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
             (i, j - 1), (i, j + 1),
             (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
        xy1 += y
    return xy1

def solve():
    global h, w, left
    initial()
    p_left = left + 1
    count = 0
    xy = [ (i, j) for j in range(1, w) for i in range(1, h)]
    while True:
        count += 1
        xy1 = wave(xy)
        if p_left == left:
            break
        p_left = left
        xy = xy1
    return count - 1

#f = open("python\input_0612-2.txt")
f = open("python\in.txt")
h, w = map(int, f.readline().split())
#h, w = map(int, input().split())

for _ in range(0, h):
    c = f.readline().strip()
    #c = input().strip()
    castle.append([int(x) if x != '.' else 0 for x in c])
ans = solve()
print(ans)
