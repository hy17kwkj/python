# http://vipprog.net/wiki/exercise.html

"""
クリティカルパス †
結合点pから結合点qまでの作業にかかる日数が列挙されているものとする。
結合点Aから結合点A+n-1(nは結合点の数: n=7のときA+n-1はG)までのクリティカルパスと
その所要日数を求めよ。
"""

nodes = 0
tasks = 0
path = []
with open("critical_path.txt") as f:
    c = 1
    for line in f:
        if c == 1:
            tmp = line.strip().split(" ")
            nodes = int(tmp[0])
            tasks = int(tmp[1])
        else:
            tmp = line.strip().split(" ")
            path.append([tmp[0], tmp[1], int(tmp[2])])
        c += 1
 
start = "A"
goal = chr(ord(start) + nodes -1)
 
def critical_path(start, goal):
    maximum = 0
    cpath = []
    for p in path:
        if p[0] == start:
            if p[1] == goal:
                maximum = p[2]
                cpath = [p[0], p[1]]
                break
            days, cp = critical_path(p[1], goal)
            days += p[2]
            if days > maximum:
                cpath = [start]
                cpath.extend(cp)
                maximum = days
    return maximum, cpath
 
cost, cp = critical_path(start, goal)
print(" -> ".join(cp))
print(cost)
