# AOJ DPL_3_A
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_3_A

m = []
s = []
f = open("python\input_dpl3a.txt")
line = f.readline()
#line = input()
h, w = list(map(int, line.split()))
s = [ [0] * w for _ in range(0, h)]
for _ in range(0, h):
    line = f.readline()
    #line = input()
    c = list(map(int, line.split()))
    m += [c]

def solve(h, w):
    ans = 0
    for y in range(0, h):
        for x in range(0, w):
            if m[y][x] == 1:
                s[y][x] = 0
            else:
                u = s[y - 1][x] if y > 0 else 0
                l = s[y][x - 1] if x > 0 else 0
                ul = s[y - 1][x - 1] if x > 0 and y > 0 else 0
                s[y][x] = 1 + min(u, l, ul)
            ans = max(ans, s[y][x])
    return ans * ans

ans = solve(h, w)
print(ans)
