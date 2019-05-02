# AOJ 2021
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2021

N = M = L = K = A = H = 0
INF = 100000000

def nexttown():
    for r in range(0, N):
        dic[r] = [t[1:3] for t in town if t[0] == r] + [ [t[0], t[2]] for t in town if t[1] == r]

def solve():
    solve2(A, M, 0)
    if mint == 100000000:
        return "Help!"
    return mint

def solve2(r, t, lv):
    global mint
    if dp[t][r] > mint:
        return
    ntown = dic[r]
    l = len(ntown)
    for i in range(0, l):
        town, time = ntown[(i + lv) % l]
#        print("town=",town,"time=",time,"lv=",lv)
        tt = t - time
        if tt >= 0:
            if not(town in freezer):
                if dp[tt][town] == 0 or min(dp[tt][town], mint) > dp[t][r] + time:
                    dp[tt][town] = dp[t][r] + time
#                    print(dp)
                    if town != H:
                        solve2(town, tt, lv + 1)
                    elif mint > dp[tt][town]:
                        mint = dp[tt][town]
            else:
                for j in range(0, M - tt + 1):
                    if dp[tt + j][town] == 0 or min(dp[tt + j][town], mint) > dp[t][r] + j + time:
#                        print("j=",j)
                        dp[tt + j][town] = dp[t][r] + j + time
#                        print(dp)
                        if town != H:
                            solve2(town, tt + j, lv + 1)
                        elif mint > dp[tt + j][town]:
                            mint = dp[tt + j][town]


f = open("python\input_2021-2.txt")
while True:
    town = []
    freezer = []
    dp = []
    dic = {}
    mint = 100000000
    line = f.readline()
    #line = input()
    N, M, L, K, A, H = map(int, line.split())
    if N == 0 and M == 0 and L == 0:
        break
    freezer = list(map(int, list(f.readline().split())))
        #freezer = list(map(int, list(input().split())))
    for _ in range(0, K):
        t = list(map(int, list(f.readline().split())))
        #t = list(map(int, list(input().split())))
        town.append(t)
    dp = [ [INF] * N for _ in range(0, M + 1) ]  
    nexttown()
    print(solve())