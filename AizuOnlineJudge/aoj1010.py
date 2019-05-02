# AOJ 1010
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1010

import sys
 
def subset(line):
    l = line.strip().split(" ")
    dominos = list(map(int, l))
    return (dominos)
 
def solve(dominos):
    for d in dominos:
        dd = (d % 10) * 10 + d // 10
        work = dominos[:]
        dominos.remove(d)
        r = solve2(d, dominos, [d])
        if r == True:
            print("Yes")
            break
        if d != dd:
            rr = solve2(dd, dominos, [dd])
            if rr == True:
                print("Yes")
                break
        dominos = work
    else:
        print("No")
  
def solve2(prev, left, used):
    #print(prev, left, used)
    if left == []:
        return True
    if prev % 10 not in list(map(lambda x: x // 10, left))         and prev % 10 not in list(map(lambda x: x % 10, left)):
        return False
    for d in left:
        if prev % 10 == d // 10:
            w_left = left[:]
            w_used = used[:]
            w_used.append(d)
            w_left.remove(d)
            r = solve2(d, w_left, w_used)
            if r == True:
                break
        if prev % 10 == d % 10 and d % 11 != 0:
            dd = (d % 10) * 10 + d // 10
            w_left = left[:]
            w_used = used[:]
            w_used.append(dd)
            w_left.remove(d)
            r = solve2(dd, w_left, w_used)
            if r == True:
                break
    else:
        return False
    return True
 
 
f = open("python\input_1010.txt")
lno = 0
for line in f:
    lno += 1
    if lno == 1:
        n = int(line)
    else:
        solve(subset(line))
        lno = 0
