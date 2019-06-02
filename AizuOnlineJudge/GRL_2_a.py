# AOJ GRL_2_A
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A

from heapq import heappush, heappop

#f = open("python\input_grl2a.txt")
f = open("python\in.txt")
line = f.readline()
#line = input()
v, e = list(map(int, line.split()))
edge = {}
edge[0] = [[0, 0]]
for _ in range(0, e):
    line = f.readline()
    #line = input()
    s, t, w = list(map(int, line.split()))
    if s not in edge:
        edge[s]  = [[t, w]]
    else:
        edge[s] += [[t, w]]
    if t not in edge:
        edge[t]  = [[s, w]]
    else:
        edge[t] += [[s, w]]

def solve(v, edge):
    q = []
    vtx = set([i for i in range(0, v)])
    for t, w in edge[0]:
        heappush(q, (w, 0, t))
    vn = set([0])
    en = []
    cost = 0
    while len(vn) < v:
        w = s = t = 0
        while q:
            w, s, t = heappop(q)
            if s in vn and t not in vn:
                s, t = t, s
                break
            if s not in vn and t in vn:
                break
        vn.add(s)
        en += [(s, t)]
        cost += w
        for t, w in edge[s]:
            heappush(q, (w, s, t))
    return cost

print(solve(v, edge))
