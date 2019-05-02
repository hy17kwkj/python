# AOJ 2021
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2021

from heapq import heappush, heappop

N = M = L = K = A = H = 0
INF = 100000000

def nexttown():
    for r in range(0, N):
        dic[r] = [t[1:3] for t in town if t[0] == r] + [ [t[0], t[2]] for t in town if t[1] == r]

def solve():
    queue = []
    heappush(queue, (0, A, M))
    while queue:
        cost, r, t = heappop(queue)
        if dp[t][r] < cost:
            continue
        ntown = dic[r]
        for nt in ntown:
            town, time = nt
            tt = t - time
            if tt < 0:
                continue
            if town in freezer:
                for j in range(0, M - tt + 1):
                    if tt + j < 0:
                        continue
                    if cost + j + time < dp[tt + j][town]:
                        dp[tt + j][town] = cost + j + time
                        heappush(queue, (cost + j + time, town, tt + j))
            else:
                if cost + time < dp[tt][town]:
                    dp[tt][town] = cost + time
                    heappush(queue, (cost + time, town, tt))
    result = min(dp[i][H] for i in range(0, M + 1))
    if result == INF:
        return "Help!"
    return result


f = open("python\input_2021-2.txt")
while True:
    freezer = []
    dp = []
    dic = []
    mint = INF
    line = f.readline()
    #line = input()
    N, M, L, K, A, H = map(int, line.split())
    if N == 0 and M == 0 and L == 0:
        break
    freezer = list(map(int, list(f.readline().split())))
        #freezer = list(map(int, list(input().split())))
    dic = [set() for _ in range(0, N)] 
    for _ in range(0, K):
        x, y, t = list(map(int, list(f.readline().split())))
        #x, y, t = list(map(int, list(input().split())))
        dic[x].add((y, t))
        dic[y].add((x, t))
    dp = [ [INF] * N for _ in range(0, M + 1) ]  
    print(solve())
