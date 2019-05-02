# AOJ 1015
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1015

import sys

class Dominating_sets:
    __bit :int = []
    __n = 0
    __answer = 0
    __nei = 0

    def __init__(self, n):
        self.__n = n
        self.__answer = n
        self.__bit = [0 for i in range(0, n)]
        self.__nei = 0

    def append(self, a, b):
        self.__bit[a] |= (1 << (self.__n - b - 1))
        self.__bit[b] |= (1 << (self.__n - a - 1))

    def is_neighborhood(self, vtx):
        self.__nei += 1
        v = vtx
        for j in range(self.__n, 0, -1):
            if v & 1 == 0:
                if self.__bit[j - 1] & vtx == 0:
                    return False
            v >>= 1
        return True

    def solve(self, v, vtx, ans):
        if ans >= self.__answer:
            return ans
        if self.is_neighborhood(vtx):
            if ans < self.__answer:
                self.__answer = ans
                #print(ans)
            return ans
        if v >= self.__n:
            return ans
        if vtx & (1 << (self.__n - v - 1)) != 0:
            return ans
        vtx_bak = vtx
        vtx |= (1 << (self.__n - v - 1))
        #print("v, vtx, ans =", v, bin(vtx), ans + 1)
        ans1 = self.__n
        ans1 = self.solve(v + 1, vtx, ans + 1)
        vtx = vtx_bak
        #vtx &= (~(1 << (self.__n - v - 1)) & 0xffffffff)
        ans2 = self.solve(v + 1, vtx, ans)
        return min(ans1, ans2)       

    def print_ans(self):
        print(self.__answer, self.__nei)

f = open("python\input_1015.txt")
while True:
    line = f.readline().split()
#    line = input().split()
    n, m = map(int, list(line))
    if n == 0 and m == 0:
        break
    domset = Dominating_sets(n)
    for _ in range(0, m):
        a, b = map(int, list(f.readline().split()))
#        a, b = map(int, list(input().split()))
        domset.append(a, b)
    domset.solve(0, 0, 0)
    domset.print_ans()
    del domset
