# http://vipprog.net/wiki/exercise.html

"""
転置行列 †
入力された行列の転置行列を求めよ
"""
a = [[1,2,3], [4,5,6], [7,8,9]]
b = []
for j in range(0,3):
    c = []
    for i in range(0,3):
        c.append(a[i][j])
    b.append(c)
