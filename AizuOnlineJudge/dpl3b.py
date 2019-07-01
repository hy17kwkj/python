# AOJ DPL_3_B
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_3_B

m = []
s = []
INF = 10000000
f = open("python\input_dpl3a.txt")
line = f.readline()
#line = input()
h, w = list(map(int, line.split()))
su = [ [(0,0)] * (w+1) for _ in range(0, h+1)]
sl = [ [(0,0)] * (w+1) for _ in range(0, h+1)]
m = [[1] * (w+1)]
for _ in range(0, h):
    line = f.readline()
    #line = input()
    c = list(map(int, line.split()))
    c = [1] + c
    m += [c]

def solve(h, w):
    ans = 0
    for y in range(1, h+1):
        for x in range(1, w+1):
            if m[y][x] == 1:
                su[y][x] = (0, 0)
                sl[y][x] = (0, 0)
            else:
                uy1, ux1 = su[y - 1][x] if y > 0 else (0, 0)
                uy2, ux2 = sl[y - 1][x] if y > 0 else (0, 0)
                ly1, lx1 = su[y][x - 1] if x > 0 else (0, 0)
                ly2, lx2 = sl[y][x - 1] if x > 0 else (0, 0)
#                ul = s[y - 1][x - 1] if x > 0 and y > 0 else 0
                if m[y - 1][x - 1] == 1:
                    su[y][x] = (uy1 + 1, 1)
                    sl[y][x] = (1, lx2 + 1)
                elif m[y - 1][x] == 1:
                    su[y][x] = (1, 1)
                    sl[y][x] = (1, lx2 + 1)
                elif m[y][x - 1] == 1:
                    su[y][x] = (uy1 + 1, 1)
                    sl[y][x] = (1, 1)
                else:
                    su[y][x] = (min(uy1 + 1, ly1), min(ux1, lx1 + 1))
                    sl[y][x] = (min(ly1, ly2 + 1), min(lx1, lx2 + 1))
            dy1, dx1 = su[y][x]
            dy2, dx2 = sl[y][x]
            ans = max(ans, dx1 * dy1, dx2 * dy2)
    return ans

ans = solve(h, w)
print(su)
print(sl)
print(ans)
