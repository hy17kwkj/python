# AOJ 1040
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1040


choco = []
max_eat = 0
max_wgt = 0
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
weight = []
max_weight = 0
dic = {}
h = w = 0

def is_connected():
    global h, w
    x, y = heart[0]
    checked = [ [0] * w for _ in range(0, h)]
    checked[y][x] = 1
#    print(choco)
    for dist in range(0, h + w - 1):
        step  = [[dist, 0]]
        if dist > 0:
            step += [ [-1, -1] for _ in range(0, dist)]
            step += [ [-1,  1] for _ in range(0, dist)]
            step += [ [ 1,  1] for _ in range(0, dist)]
            step += [ [ 1, -1] for _ in range(0, dist)]
        x1, y1 = x, y
        for st in step:
            x1 += st[0]
            y1 += st[1]
            if not (0 <= x1 < w and 0 <= y1 < h):
                continue
            for d in range(0, 4):
                xd = x1 + dx[d]
                yd = y1 + dy[d]
                if 0 <= xd < w and 0 <= yd < h:
                    if choco[y1][x1] > 0 and checked[y1][x1] >= 0:
                        if choco[yd][xd] > 0:
                            checked[yd][xd] = dist + 1
                            continue
                    elif checked[yd][xd] > 0:
                        continue
                    checked[yd][xd] = -1
    for x, y in heart[1:]:
        if checked[y][x] <= 0:
            return False
#    print("T")
    return True


"""
def is_connected():
    global h, w
#    print(choco)
    for x, y in heart:
        checked = [ [0] * w for _ in range(0, h)]
#        print("X=",x,"Y=",y)
        checked[y][x] = 1
        if not is_connected2(x, y, checked):
            return False
    return True

def is_connected2(x, y, checked):
    global h, w
    for d in range(0, 4):
        x1 = x + dx[d]
        y1 = y + dy[d]
        if 0 <= x1 < w and 0 <= y1 < h and checked[y1][x1] == 0:
            checked[y1][x1] = 1
            if choco[y1][x1] == 1:
#                print("[T] x=",x,"y=",y)
                return True
            elif choco[y1][x1] == 2:
                if is_connected2(x1, y1, checked):
                    return True
#    print("[F] x=",x,"y=",y)
    return False
"""

def init():
    global h, w, weight, weight_list, max_weight, dic
    weight = [ [0] * w for _ in range(0, h)]
    for i in range(0, len(heart)):
        x1, y1 = heart[i]
        for j in range(i + 1, len(heart)):
            x2, y2 = heart[j]
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1
            for k in range(y1, y2 + 1):
                for l in range(x1, x2 + 1):
                    weight[k][l] += 1
    max_weight = max(max(weight[i]) for i in range(0, h))
    for wgt in range(max_weight, -1, -1):
        item = []
        for i in range(0, h):
            for j in range(0, w):
                if weight[i][j] == wgt:
                    item += [(i, j)]
        dic[wgt] = item
#    print(weight)

def solve(idx, eat, wgt):
    global max_eat, max_wgt
    if wgt < max_wgt or eat <= max_eat:
        return
#    print(dic[wgt][idx], eat, wgt)
#    print(choco)
    #"""
    if is_connected():
        if eat > max_eat:
            max_eat = eat
            max_wgt = wgt
        return
    #"""
    y, x = dic[wgt][idx]
    if choco[y][x] == 0 and weight[y][x] == wgt:
        choco[y][x] = 2
        """
        if is_connected():
            if eat - 1 > max_eat:
                max_eat = eat - 1
                max_wgt = wgt
            return
        """
        #if is_connected():
        solve(idx, eat - 1, wgt)
        choco[y][x] = 0

    w1 = wgt
    idx1 = idx + 1
    while w1 >= 0:
        while idx1 < len(dic[w1]):
#            print("wgt=",w1)
            solve(idx1, eat, w1)
            return
        idx1 = 0
        w1 -= 1
    return


f = open("python\input_1040.txt")
while True:
    choco = []
    heart = []
    weight = []
    weight_list = []
    dic = {}
    max_eat = 0
    max_wgt = 0
    max_weight = 0
    line = f.readline()
#    line = input()
    h, w = list(map(int, list(line.split())))
    if h == 0 and w == 0:
        break
    for _ in range(0, h):
        a = list(map(int, list(f.readline().split())))
#        a = list(map(int, list(input().split())))
        choco.append(a)
    for j in range(0, h):
        for i in range(0, w):
            if choco[j][i] == 1:
                heart += [(i, j)]
    init()
    eat = h * w - sum(choco[i].count(1) for i in range(0, h)) 
    solve(0, eat, max_weight)
    print(max_eat)
