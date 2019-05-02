# AOJ 0509
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0509

import sys

class Sheets:
    __rect = []
    __n = 0
    __r = 0
    __x = []
    __y = []

    def __init__(self, n, r):
        self.__n = n
        self.__r = r
        self.__rect = []
        self.__x = []
        self.__y = []

    def append(self, x1, y1, x2, y2):
        self.__rect.append([x1, y1, x2, y2])

    def is_contained_rect(self, r, x1, y1, x2, y2):
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        if r[0] <= x1 and x2 <= r[2] and r[1] <= y1 and y2 <= r[3]:
            return True
        return False

    def is_contained_pt(self, r, x, y):
        return self.is_contained_rect(r, x, y, x, y)

    def on_boundary_line(self, rect, x1, y1, x2, y2):
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        if x1 != x2 and y1 != y2:
            return False
        a = b = -1
        if y1 == y2:
            m = (x1 + x2) / 2
            for r in rect:
                if self.is_contained_pt(r, m, y1 - .5):
                    a = 1
                    break
            for r in rect:
                if self.is_contained_pt(r, m, y1 + .5):
                    b = 1
                    break
        if x1 == x2:
            m = (y1 + y2) / 2
            for r in rect:
                if self.is_contained_pt(r, x1 - .5, m):
                    a = 1
                    break
            for r in rect:
                if self.is_contained_pt(r, x1 + .5, m):
                    b = 1
                    break
        return a * b == -1

    def area(self):
        area = 0
        self.__x = [r[0] for r in self.__rect] + [r[2] for r in self.__rect]
        self.__y = [r[1] for r in self.__rect] + [r[3] for r in self.__rect]
        self.__x = list(set(self.__x))
        self.__y = list(set(self.__y))
        self.__x.sort()
        self.__y.sort()
        x1 = self.__x[0]
        for x2 in self.__x[1:]:
            rect = [r for r in self.__rect if r[0] <= x1 and x2 <= r[2] ]
            y = [r[1] for r in rect] + [r[3] for r in rect]
            y.sort()
            y1 = y[0]
            for y2 in y[1:]:
                for r in rect:
                    if self.is_contained_rect(r, x1, y1, x2, y2):
                        area += (x2 - x1) * (y2 - y1)
                        break
                y1 = y2
            x1 = x2
        return area

    def circum(self):
        circ = 0
        for x in self.__x:
            rect = [r for r in self.__rect if r[0] <= x <= r[2]]
            y = [r[1] for r in rect] + [r[3] for r in rect]
            y.sort()
            y1 = y[0]
            for y2 in y[1:]:
                if self.on_boundary_line(rect, x, y1, x, y2):
                    circ += (y2 - y1)
                y1 = y2
        for y in self.__y:
            rect = [r for r in self.__rect if r[1] <= y <= r[3]]
            x = [r[0] for r in rect] + [r[2] for r in rect]
            x.sort()
            x1 = x[0]
            for x2 in x[1:]:
                if self.on_boundary_line(rect, x1, y, x2, y):
                    circ += (x2 - x1)
                x1 = x2
        return circ


f = open("python\input_0509.txt")
while True:
    line = f.readline().split()
#    line = input().split()
    n, r = map(int, list(line))
    if n == 0 and r == 0:
        break
    sheets = Sheets(n, r)
    for _ in range(0, n):
        a, b, c, d = map(int, list(f.readline().split()))
#        a, b, c, d = map(int, list(input().split()))
        sheets.append(a, b, c, d)
    print(sheets.area())
    if r == 2:
        print(sheets.circum())
    del sheets
