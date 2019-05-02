# http://vipprog.net/wiki/exercise.html

"""
線形合同法 †
線形合同法を用いて0<=x<1の範囲の乱数を発生させるプログラムを作成せよ。
M＝65536(=2^16),A=997,B=1,Xの初期値を12345として100個の乱数を発生させ,
その値と平均を出力しなさい。
"""

def my_rand(n):
    x0 = 12345
    for i in range(0, n):
        x = (997 * x0 + 1) & 0xffff
        yield (x / 65536)
        x0 = x
 
a = [x for x in my_rand(100)]
print(a)
print(sum(a) / 100)
