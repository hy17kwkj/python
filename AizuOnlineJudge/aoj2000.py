# AOJ 2000
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2000
 
import sys
 
def move(cmd, gems):
    n = 0
    x = y = 10
    for c in cmd:
        d = c[0]
        l = c[1]
        for s in range(0, l):
            if d == "N":
                y += 1
            elif d == "E":
                x += 1
            elif d == "S":
                y -= 1
           elif d == "W":
                x -= 1
            if gems[y][x] == 1:
                n += 1
                gems[y][x] = 0
    return n
 
gems = []
cmd = []
f = open("python\input_2000.txt")
att = "gemsN"
for line in f:
    if att =="gemsN":
        n = w_n = int(line)
        if n == 0:
            break
        att = "gemsXY"
        gems = [[0 for i in range(0,21)] for j in range(0,21)]
    elif att == "gemsXY" and w_n > 0:
        xy = list(map(int, line.strip().split(" ")))
        gems[xy[1]][xy[0]] = 1
        w_n -= 1
    elif att == "gemsXY" and w_n == 0:
        att = "cmd"
        cmd = []
        m = int(line)
    elif att == "cmd" and m > 0:
        dl = line.strip().split(" ")
        cmd.append([dl[0], int(dl[1])])
        m -= 1
        if m == 0:
            a = move(cmd, gems)
            ans = "Yes" if a == n else "No"
            print(ans)
            att = "gemsN"
