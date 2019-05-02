# AOJ 1128
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1128

import sys
import copy
import numpy as np

class Carpet:
    __room = []
    __put = []
    __count = []
    __index = []
    __dic = {}
    __w = __h = 0
    __maxsize = 0
    __answer = 0
    __scratched = 0

    def __init__(self, width, height):
        self.__w = width
        self.__h = height
        self.__maxsize = min(width, height)
        self.__answer = width * height
        self.__put = np.zeros((height, width), dtype = int)
        self.__count = np.zeros((height, width), dtype = int)
        self.__room = np.array([], dtype = int)
        self.__scratched = width * height
        self.__index = []
        self.__dic = {}


    def append(self, line):
        row = list(map(int, list(line)))
        r = np.array(list(map(lambda x: -1 if x == 0 else 0, row)), dtype = int)
        self.__room = np.append(self.__room, r, axis=0)

    def size(self):
        self.__room = self.__room.reshape(self.__h, self.__w)
        for j in range(0, self.__h):
            for i in range(0, self.__w):
                if self.__room[j][i] == -1:
                    self.__scratched -= 1
                    continue
                for size in range(self.__maxsize, 0, -1):
                    if i + size > self.__w or j + size > self.__h:
                        continue
                    tmp = self.__room[j:j + size, i:i + size]
                    if np.all(tmp == 0):
                        self.__put[j][i] = size
                        self.add_count(i, j, size)
                        break
        print("room=", self.__room)
        print("put=", self.__put)
        print("count=",self.__count)

    def add_count(self, i, j, size):
        self.__count[j:j + size, i:i + size] += 1

    def sub_count(self, i, j, size):
        self.__count[j:j + size, i:i + size] -= 1

    def put(self, i, j, size, n):
        tmp = self.__room[j:j + size, i:i + size]
        tmp[tmp == 0] = n
        c = len(np.where(tmp == n)[0])
        return c

    def remove(self, i, j, size, n):
        tmp = self.__room[j:j + size, i:i + size]
        tmp[tmp == n] = 0
        r = len(np.where(tmp == 0)[0])
        return r

    def contained(self, i, j, size):
        tmp = self.__room[j:j + size, i:i + size]
        return not(np.any(tmp == 0))

    def compress(self):
        tmp = np.where(self.__room != 0, '1', '0').flatten().tolist()
        return hash("".join(tmp))

    def solve(self):
        init_answer = 0
        for j in range(0, self.__h):
            for i in range(0, self.__w):
                if self.__count[j][i] == 1 and self.__room[j][i] == 0:
                    size = self.__put[j][i]
                    init_answer += 1
                    self.put(i, j, size, init_answer)

        print(self.__room)
        for j in range(0, self.__h):
            for i in range(0, self.__w):
                if self.__count[j][i] == 0:
                    continue
                size = self.__put[j][i]
                if self.contained(i, j, size) == False:
                    break
                else:
                    self.__put[j][i] = 0
                    self.sub_count(i, j, size)

        covered = 0
        for j in range(0, self.__h):
            for i in range(0, self.__w):
                if self.__room[j][i] > 0:
                    covered += 1
                if self.__put[j][i] > 0:
                    self.__index.append([i, j])
        print(self.__index)

        print(self.__room)
        self.solve2(0, init_answer, covered)
        print(self.__answer)

    def solve2(self, idx, ans, covered):
        if ans >= self.__answer:
            return ans
        if covered == self.__scratched:
            print("ans = ", ans)
            if self.__answer > ans:
                self.__answer = ans
            return ans
        while idx < len(self.__index):
            x, y = self.__index[idx]
            size = self.__put[y][x]
            if size > 0 and self.contained(x, y, size) == False:
                ans1 = ans2 = self.__h * self.__w
                if ans + 1 < self.__answer:
                    #print("x, y, size, ans, __ans =", x, y, size, ans+1, self.__answer)
                    c = self.put(x, y, size, ans + 1)
                    """
                    cmp = self.compress()
                    if cmp in self.__dic and self.__dic[cmp] <= ans + 1:
                        self.remove(x, y, size, ans + 1)
                        return ans

                    self.__dic[cmp] = ans + 1
                    """
                    covered += c
                    #print("put = ", self.__room)
                    ans1 = self.solve2(idx + 1, ans + 1, covered)
                    r = self.remove(x, y, size, ans + 1)
                    covered -= r
                    #print("remove = ", self.__room)
                if ans < self.__answer:
                    ans2 = self.solve2(idx + 1, ans, covered)
                ans = min(ans1, ans2)
                return ans

            idx += 1
        return ans


f = open("python\input_1128.txt")
while True:
    line = f.readline().split()
#    line = input().split()
    w, h = map(int, list(line))
    if w == 0 and h == 0:
        break
    carpet = Carpet(w, h)
    for _ in range(0, h):
        line = f.readline().split()
#        line = input().split()
        carpet.append(list(map(int, list(line))))
    carpet.size()
    carpet.solve()
    del carpet
