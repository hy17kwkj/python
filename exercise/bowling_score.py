# http://vipprog.net/wiki/exercise.html

"""
ボウリングのスコア計算2 †
ボウリングのスコアを計算し、各フレームでそのフレームまでのスコアを出力する。
1行目は投げた回数、2行目は倒したピンの数が入力される。
不正な値は入力されないものとする。
"""

throw = int(input("投球回数 >> "))
pins = input("倒したピンの数 >> ")
 
p = list(map(int, list(pins.split(" "))))
if len(p) != throw:
    print("投球回数エラー")
    sys.exit
 
score = 0
n = 0
frame = 0
while frame < 10:
    frame += 1
    score += p[n]
    if p[n] == 10:
        score += p[n+1] + p[n+2]
        n += 1
    else:
        score += p[n+1]
        if p[n] + p[n+1] == 10:
            score += p[n+2]
        n += 2
    print(score, end = " ")
