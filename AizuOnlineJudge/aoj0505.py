# AOJ0505
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0505

enqu = []
n = m = 0

def solve():
    score = [ sum(enqu[i][j] for i in range(0, n)) for j in range(0, m)]
    x = [ [j + 1, score[j]] for j in range(0, m)]
    x.sort(key = lambda y: y[1], reverse=True)
    print(" ".join(list(map(lambda y: str(y[0]), x))))


f = open("python\input_0505.txt")
while True:
    enqu = []
    line = f.readline()
    #line = input().split()
    n, m = map(int, line.split())
    if n == 0 and m == 0:
        break

        for _ in range(0, n):
        answer = list(map(int, list(f.readline().split())))
        #answer = list(map(int, list(input().split())))
        enqu.append(answer)
    solve()