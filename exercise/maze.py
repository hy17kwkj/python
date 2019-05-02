# http://vipprog.net/wiki/exercise.html

"""
迷路を解くプログラム †
http://www.logsoku.com/r/news4vip/1377327045/61-66n
10 x 10の迷路を解く
入力は、4辺のどこか2箇所が必ず開いている（スタートorゴール）ものとする
移動方向は縦横のみ、斜めはなし
"""
from functools import reduce
 
maze = [\
"# ########",\
"# ## ### #",\
"#    ##  #",\
"####    ##",\
"# ## #####",\
"#    #   #",\
"# #### # #",\
"#      # #",\
"## ## ## #",\
"######## #"]
 

SizeX, SizeY = 10, 10
m = [0] * (SizeX * SizeY)
m = [[0 if maze[y][x] == '#' else -1 for x in range(0, SizeX)] for y in range(0, SizeY)]
 
def step(x, y, dirc):
    nx, ny = x, y
    if dirc & 1:
        if SizeX - 2 >= x and m[y][x + 1] < 0:
            nx = x + 1
    elif dirc & 2:
        if SizeY - 2 >= y and m[y + 1][x] < 0:
            ny = y + 1
    elif dirc & 4:
        if x - 1 >= 0 and m[y][x - 1] < 0:
            nx = x - 1
    elif dirc & 8:
        if y - 1 >= 0 and m[y - 1][x] < 0:
            ny = y - 1
    return (nx, ny)
 
def is_branch(x, y):
    dirc = []
    if SizeX - 2 >= x and m[y][x + 1] < 0:
        dirc.append(1)
    if SizeY - 2 >= y and m[y + 1][x] < 0:
        dirc.append(2)
    if x - 1 >= 0 and m[y][x - 1] < 0:
        dirc.append(4)
    if y - 1 >= 0 and m[y - 1][x] < 0:
        dirc.append(8)
    return (dirc)
 
def go_next_branch(x, y):
    route = [[x, y]]
    dirc = []
    l = 1
    while l == 1:
        dirc = is_branch(x, y)
        l = len(dirc)
        if l >= 1:
            m[y][x] = reduce(lambda x, y: x ^ y, dirc)
            if l == 1:
                x, y = step(x, y, dirc[0])
                route.append([x, y])
    return (l, dirc, route)
 
def solve(r, sx, sy, gx, gy):
    x, y = sx, sy
    route = r
    while True:
        l, dirc, r = go_next_branch(x, y)
        print("solve", l, dirc, r)
        if l == 0:
            if r[-1][0] == gx and r[-1][1] == gy:
                route.extend(r)
                return (route)
            break
        elif l > 1:
            route.extend(r)
            x, y = r[-1]
            for d in dirc:
                nx, ny = step(x, y, d)
                route = solve(route, nx, ny, gx, gy)
    return (route)
       
sx, sy = 1, 0
gx, gy = 8, 9
x, y = sx, sy
route = []
route = solve([], sx, sy, gx, gy)
print(route)
 
for y in range(0, SizeY):
    for x in range(0, SizeX):
        c = maze[y][x]
        if c == '#':
            print('#', end='')
        elif [x, y] in route:
            print('+', end='')
        else:
            print(' ', end='')
    print('')
