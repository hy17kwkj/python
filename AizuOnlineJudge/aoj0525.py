# AOJ0525
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0525

import array

r = 0
c = 0
senbei = []

def solve():
    res = 0
    for n in range(0, 2 ** r):
        rev = [(n >> i) & 1 for i in range(0, r)]
        tsenbei = [ [ 1 - senbei[i][j] if rev[i] == 1 else senbei[i][j]                     for i in range(0, r)]                   for j in range(0, c)]
        s1 = [sum(tsenbei[j]) for j in range(0, c)]
#        s1 = array.array('i', [sum(abs(rev[i] - senbei[i * c + j]) for i in range(0, r)) \
#                           for j in range(0, c)])
        a = sum(max(s1[j], r - s1[j]) for j in range(0, c))
        if a > res:
            res = a
    return res

if __name__ == '__main__':
    f= open("python\input_0525.txt")
    while True:
        line = f.readline()
#        line = input()
        r, c = map(int, line.split())
        if r == 0 and c == 0:
            break
        senbei = []
        for _ in range(0, r):
            row = list(map(int, list(f.readline().split())))
#            row = list(map(int, list(input().split())))
            senbei.append(row)
        print(solve())
