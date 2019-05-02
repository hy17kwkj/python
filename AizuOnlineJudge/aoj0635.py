# AOJ0635
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0635

corr = []
temp = []
dp = []
dic = {}
mint = 100000000

def nextroom():
    for r in range(1, n + 1):
        dic[r] = [c[1:3] for c in corr if c[0] == r] + [ [c[0], c[2]] for c in corr if c[1] == r]

def solve():
    solve2(1, x, 0 , 0)
    return mint

def solve2(r, t, hc, lv):
    global mint
    nroom = dic[r]
#    print("r=",r,"t=",t,nroom)
    for nr in nroom:
        room, time = nr
        tt = t - time if t - time > 0 else 0
#        print("tt=",tt,"r=",r,"room=",room,"lv=",lv)
#        print("dp[t][r]=", dp[t][r], "dp[tt][room]=", dp[tt][room])
        if (temp[room] != 1 and temp[room] != hc and tt == 0) or temp[room] == 1 or            (temp[room] != 1 and temp[room] == hc):
            tt = tt if temp[room] == 1 or temp[room] == hc else x
#            print("tt'=",tt)
            if dp[tt][room] == 0 or min(dp[tt][room], mint) > dp[t][r] + time:
                dp[tt][room] = dp[t][r] + time
#                print(r,"->",room, hc)
#                print(dp)
                if room != n:
                    solve2(room, tt, temp[room] if tt == x else hc, lv+1)
                elif mint > dp[tt][room]:
                    mint = dp[tt][room]
                    print(mint)


f = open("python\input_0635-2.txt")
line = f.readline()
#line = input()
n, m, x = map(int, line.split())
temp = [-1]
for _ in range(0, n):
    t = f.readline()
    #t = input()
    temp.append(int(t))
for _ in range(0, m):
    c = list(map(int, list(f.readline().split())))
    #c = list(map(int, list(input().split())))
    corr.append(c)
dp = [ [0] * (n + 1) for _ in range(0, x + 1) ]  
nextroom()
solve()