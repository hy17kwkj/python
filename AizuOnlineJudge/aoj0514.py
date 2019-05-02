# AOJ0514
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0514

import sys

class QualityChecking:
    def __init__(self, a, b, c, N):
        self.__N = N
        self.__a = a
        self.__b = b
        self.__c = c
        self.__test = []

    def read(self, i, j, k, r):
        self.__test.append([i, j, k, r])

    def solve(self):
        ok = set()
        ng = set()
        for t in self.__test:
            if t[3] == 1:
                ok.add(t[0])
                ok.add(t[1])
                ok.add(t[2])
        test1 = []
        for t in self.__test:
            test1.append(["ok" if x in ok else x for x in t])
        for t in test1:
            if t[3] == 0:
                if t[0] == "ok" and t[1] == "ok":
                    ng.add(t[2])
                elif t[0] == "ok" and t[2] == "ok":
                    ng.add(t[1])
                elif t[1] == "ok" and t[2] == "ok":
                    ng.add(t[0])
        for i in range(1, self.__a + self.__b + self.__c + 1):
            if i in ok:
                print("1")
            elif i in ng:
                print("0")
            else:
                print("2")


f = open("python\input_0514.txt")
while True:
    line = f.readline()
#    line = input()
    a, b, c = map(int, list(line.split()))
    if a == 0 and b == 0 and c == 0:
        break
    line = f.readline()
#    line = input()
    n = int(line)
    qc = QualityChecking(a, b, c, n)
    for _ in range(0, n):
        i, j, k, r = map(int, list(f.readline().split()))
#        i, j, k, r = map(int, list(input().split()))
        qc.read(i, j, k, r)
    qc.solve()
    del qc
