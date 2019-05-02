# AOJ0520
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0520

import sys

def gcd(x, y):
    if x < y:
        x, y = y, x
    while x % y != 0:
        x, y = y, x % y
    return y

class frac:
    def __init__(self, n, d):
        self.num = n
        self.den = d

    def mul(self, yn, yd):
        xn, xd = self.num, self.den
        xn *= yn
        xd *= yd
        if xn != 0 and xd != 0:
            g = gcd(xn, xd)
            xn /= g
            xd /= g
        return frac(xn, xd)

    def is_zero(self):
        return self.num == 0

    def output(self):
        return "{}/{}".format(self.num, self.den)      

class LightestMobile:
    def __init__(self, n):
        self.n = n + 1
        self.mobile = [[0,0,0,0]]
        self.weight = [[frac(0,1), frac(0,1)]]
        self.denom = []

    def read(self, p, q, r, b):
        self.mobile.append([p, q, r, b])
        self.weight.append([frac(0,1), frac(0,1)])


    def root(self):
        for i in range(1, self.n):
            m = self.mobile[i]
            if m[2] == 0 and m[3] == 0:
                return self.parent(i)

    def parent(self, c):
        for i in range(1, self.n):
            m = self.mobile[i]
            if i != c and (m[2] == c or m[3] == c):
                return self.parent(i)
        return c

    def solve(self, i):
        self.solve2(i, frac(0,1))
        lcm = 1
        for d in self.denom:
            lcm = lcm * d / gcd(lcm, d)
        answer = self.weight[i][0].mul(lcm, 1).num + self.weight[i][1].mul(lcm, 1).num
        return int(answer)

    def solve2(self, i, wlr):
        p, q, r, b = self.mobile[i]
#        print("p,q,r,b=", self.mobile[i])
#        print("i, wlr=", i, wlr.output())
        if wlr.is_zero():
            g = gcd(p, q)
            p /= g
            q /= g
            self.weight[i] = [frac(q, 1), frac(p, 1)]
        else:
            self.weight[i] = [wlr.mul(q, p + q), wlr.mul(p, p + q)]
        if r != 0:
            self.solve2(r, self.weight[i][0])
        if b != 0:
            self.solve2(b, self.weight[i][1])
        if r == 0 and b == 0:
            if not self.weight[i][0].is_zero() and not self.weight[i][1].is_zero():
                self.denom.append(self.weight[i][0].den)
                self.denom.append(self.weight[i][1].den)
        return

if __name__ == '__main__':
    f = open("python\input_0520.txt")
    while True:
        line = f.readline()
#        line = input()
        n = int(line)
        if n == 0:
            break
        lm = LightestMobile(n)
        for _ in range(0, n):
            p, q, r, b = map(int, list(f.readline().split()))
#            p, q, r, b = map(int, list(input().split()))
            lm.read(p, q, r, b)
        rt = lm.root()
        print(lm.solve(rt))
        del lm
