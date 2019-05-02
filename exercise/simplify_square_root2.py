# http://vipprog.net/wiki/exercise.html

"""
有理化するプログラム †
√a/√bを有理化せよ。
aは[1, 100]、bは[2, 100]とする。
"""

A = 10
B = 10
 
def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return (b)
 
def rationalization(a, b):
    d, r = div_square(a * b, int(math.sqrt(A * B)))
    gd = gcd(d, b)
#    print(d, r, gd)
    d /= gd
    b /= gd
    return int(d), r, int(b)
 
for a in range(1, A + 1):
    for b in range(2, B + 1):
        d, r, bb = rationalization(a, b)
       # print(d,r,bb)
        print("√{}/√{} -> ".format(a, b), end="")
        num = ""
        den = ""
        if d != 1 or r == 1:
            num += "{}".format(d)
        if r != 1:
            num += "√{}".format(r)
        if bb != 1:
            den = "/{}".format(bb)
        print(num + den)
