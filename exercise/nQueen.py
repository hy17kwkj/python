# http://vipprog.net/wiki/exercise.html

"""
Nクイーン問題 †
http://www.logsoku.com/r/news4vip/1379246445/1n
7x7のマス目にチェスのクイーンがお互いを取り合うことのないようにできる限りの
数置くことを考える。
入力例のように既に2つのクイーン(Q)が置かれているとき、どのように置けばよいか。
入力例
.......
.......
..Q....
.......
...Q...
.......
.......
"""
board = [\
".......",\
".......",\
"..Q....",\
".......",\
"...Q...",\
".......",\
".......",\
]

b = [board[i].find("Q") for i in range(0,7)]
Size = 7
 
def is_queen_ok(y, x, b):
    if b[y] >= 0:
        return False
    if x in b:
        return False
    for qy, qx in enumerate(b):
        #print(qy, qx)
        if qx != -1:
            if qx - x == qy - y:
                return False
            if qx - x == -(qy - y):
                return False
            if -(qx - x) == qy - y:
                return False
            if -(qx - x) == -(qy - y):
                return False
    return True
 
ng = []
def nqueen(n, b):
    if n == 0:
        return b
    if b[n - 1] >= 0:
        return nqueen(n - 1, b)
    for x in range(0, Size):
        if is_queen_ok(n - 1, x, b):
            #print(n, x)
            bak = b[:]
            b[n - 1] = x
            #print(b, bak)
            nq = nqueen(n - 1, b)
            if nq == []:
                b = bak
                continue
            return nq
    return []
 
nqueen(7, b)
