# aoj0628
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0628

area = set()
walk = set()

def route(w, k):
    x = y = 0
    walk.add((0, 0))
    for i in range(0, k):
        for d in w:
            if d == 'E':
                x += 1
            elif d == 'N':
                y += 1
            elif d == 'W':
                x -= 1
            elif d == 'S':
                y -= 1
            walk.add((x, y))
    return walk

def isarea(cx, cy):
    if (cx, cy) in area:
        return
    x1, y1 = cx - 0.5, cy - 0.5
    x2, y2 = cx + 0.5, cy + 0.5
    sq = set([(x1, y1), (x1, y2), (x2, y1), (x2, y2)])
    if sq <= walk:
        area.add((cx, cy))

def solve():
    for x, y in walk:
        isarea(x + 0.5, y + 0.5)
        isarea(x - 0.5, y + 0.5)
        isarea(x - 0.5, y - 0.5)
        isarea(x + 0.5, y - 0.5)
    return len(area)

f = open("python\input_0628-1.txt")
walk = set()
area = set()
line = f.readline()
#line = input()
n, k = map(int, line.split())
w = f.readline()
#w = input()
route(w, k)
print(solve())
