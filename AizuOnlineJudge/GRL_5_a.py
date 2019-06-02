# AOJ GRL_5_A
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_A

def solve(prev, r, dic):
    d = 0
    t = r
    stack = []
    stack += [[prev, r, d]]
    while stack:
        prev, r, d1 = stack.pop(-1)
        if r in dic:
            for vtx, cost in dic[r]:
                if vtx == prev:
                    continue
                stack += [[r, vtx, d1 + cost]]
                if d < d1 + cost:
                    d = d1 + cost
                    t = vtx
    return d, t


#f = open("python\input_grl5a.txt")
f = open("python\in18.txt")
dp = []
line = f.readline()
#line = input()
n = int(line)
edge = {}
for _ in range(0, n - 1):
    line = f.readline()
    #line = input()
    s, t, d = list(map(int, line.split()))
    if s not in edge:
        edge[s] = [[t, d]]
    else:
        edge[s] += [[t, d]]
    if t not in edge:
        edge[t] = [[s, d]]
    else:
        edge[t] += [[s, d]]
r1, t1 = solve(-1, 0, edge)
r2, t2 = solve(-1, t1, edge)
print(r2)