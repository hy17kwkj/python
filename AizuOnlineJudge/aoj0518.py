# AOJ 0518
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0518

import sys

class Site:
    def __init__(self, n):
        self.__piller = set()
        self.__n = n

    def append(self, x, y):
        self.__piller.add((x, y))

    def area(self, xy1, xy2):
        dx = xy1[0] - xy2[0]
        dy = xy1[1] - xy2[1]
        return dx * dx + dy * dy

    def square1(self, xy1, xy2):
        x1, y1 = xy1
        x2, y2 = xy2
        dx, dy = x2 - x1, y2 - y1
        return {(x1 - dy, y1 + dx), (x1 - dy + dx, y1 + dx + dy)}

    def square2(self, xy1, xy2):
        x1, y1 = xy1
        x2, y2 = xy2
        dx, dy = x2 - x1, y2 - y1
        return {(x1 + dy, y1 - dx), (x1 + dy + dx, y1 - dx + dy)}

    def square(self, xy):
        pass

    def solve(self):
        """
        dic = {}
        for xy1 in self.__piller:
            for xy2 in self.__piller:
                k = self.area(xy1, xy2)
                if k in dic:
                    #dic[k].add(xy1)
                    #dic[k].add(xy2)
                    dic[k] += 1
                else:
                    #dic[k] = {xy1, xy2}
                    dic[k] = 1
        #cand = {k:dic[k] for k in dic if len(dic[k]) == 4}
        cand = {k for k in dic if dic[k] == 8}
        area = 0
        for k in cand:
            #print(k, cand[k])
            if k > area:
                area = k
        """
        area = 0
        for xy1 in self.__piller:
            pil = {xy for xy in self.__piller if self.area(xy1, xy) > area                    and (self.square1(xy1, xy).issubset(self.__piller)                         or self.square2(xy1, xy).issubset(self.__piller))}
            for xy2 in pil:
                a = self.area(xy1, xy2) 
                if a > area:
                    area = a
        #"""
        return area

f = open("python\input_0518.txt")
while True:
    line = f.readline()
#    line = input()
    n = int(line)
    if n == 0:
        break
    site = Site(n)
    for _ in range(0, n):
        x, y = map(int, list(f.readline().split()))
#        x, y = map(int, list(input().split()))
        site.append(x, y)
    print(site.solve())
    del site
