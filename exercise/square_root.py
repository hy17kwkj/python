# http://vipprog.net/wiki/exercise.html

"""
平方根を求めてみる †
与えられた数の平方根を求める
当然ライブラリは使わない
"""
a = float(input("a = >> "))
x = a
x1 = 0
while True:
    x1 =  x / 2.0 + a / (2.0 * x)
    if abs(x - x1) < 1e-30:
        break
    x = x1

rint("sqrt(%f) = %f" % (a, x))
x
