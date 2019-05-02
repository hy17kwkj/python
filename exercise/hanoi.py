# http://vipprog.net/wiki/exercise.html

"""

ハノイの塔 †
与えられたn枚の円盤を用いたハノイの塔を再帰的アルゴリズムを用いて解く
プログラムを作成せよ。出力は円盤の移動の記録及び手数とする。
"""

def hanoi(n, fr, to):
    tmp = 0
    if (fr == 1 and to == 2) or (fr == 2 and to == 1):
        tmp = 3
    elif (fr == 1 and to == 3) or (fr == 3 and to == 1):
        tmp = 2
    elif (fr == 2 and to == 3) or (fr == 3 and to == 2):
        tmp = 1
 
    if n <= 1:
        ans = ["{}->{}".format(fr, to)]
    elif n == 2:
        ans = ["{}->{}".format(fr, tmp)]
        ans += ["{}->{}".format(fr, to)]
        ans += ["{}->{}".format(tmp, to)]
    else:
        ans = hanoi(n - 1, fr, tmp)
        ans += ["{}->{}".format(fr, to)]
        ans += hanoi(n - 1, tmp, to)
    return (ans)
 
