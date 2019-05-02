# AOJ 0529
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0529

class Darts:
    def __init__(self, n, m):
        self.__n = n
        self.__m = m
        self.__p = []

    def append(self, p):
        self.__p.extend(p)

    def solve(self):
        self.__p.append(0)
        p2 = set()
        for b in self.__p:
            for a in self.__p:
                p2.add(a + b)
        p2 = list(p2)
        p2.sort()
        ans = 0
        for j in p2:
            a = 0
            b = 0
            e = len(p2) - 1
            while e - b > 1:
                mid = (b + e) >> 1
                if self.__m - j < p2[mid]:
                    e = mid
                elif p2[mid] < self.__m - j:
                    b = mid
                elif p2[mid] == self.__m - j:
                    return self.__m
            if e - b == 1 and p2[b] <= self.__m - j < p2[e]:
                a = j + p2[b]
                if a > ans:
                    ans = a
        return ans

f = open("python\input_0529.txt")
while True:
    line = f.readline().split()
#    line = input().split()
    n, p = map(int, list(line))
    if n == 0 and p == 0:
        break
    darts = Darts(n, p)
    for _ in range(0, n):
        a = map(int, list(f.readline().split()))
#        a = map(int, list(input().split()))
        darts.append(a)
    print(darts.solve())
    del darts