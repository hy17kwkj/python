# AOJ 1034
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1034

board = []
used = []
v = []
n = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def set_v():
    global v
    for y in range(0, n):
        for x in range(0, n):
            if board[y][x] < 0:
                v += [(x, y)]
                used[y][x] = 1 

def solve(x, y, rest, s, k):
    #print(x,y,rest,s,k)
    #print(used)
    if s == 0:
        if rest == 0:
            if k == len(v) - 1:
                return True
            return False
        if k < len(v) - 1:
            k1 = k + 1
            xx, yy = v[k1]
            used[y][x] = 1
            if solve(xx, yy, rest - 1, - board[yy][xx], k1):
                return True
            used[y][x] = 0
    if s <= 0 or k >= len(v):
        return False
    if board[y][x] > 0:
        used[y][x] = 1
    for d in range(0, 4):
        xx = x + dx[d]
        yy = y + dy[d]
        if 0 <= xx < n and 0 <= yy < n and used[yy][xx] == 0:
            if solve(xx, yy, rest - 1, s - board[yy][xx], k):
                return True
    if board[y][x] > 0:
        used[y][x] = 0
    return False



f = open("python\input_1034.txt")
while True:
    board = []
    v = []
    line = f.readline()
#    line = input()
    n = int(line)
    if n == 0:
        break
    for _ in range(0, n):
        a = list(map(int, list(f.readline().split())))
#        a = list(map(int, list(input().split())))
        board.append(a)
    used = [ [0] * n for _ in range(0, n)]
    set_v()
    x, y = v[0]
    print("YES" if solve(x, y, n * n - 1, - board[y][x], 0) else "NO")
