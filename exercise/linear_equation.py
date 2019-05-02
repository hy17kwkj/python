# http://vipprog.net/wiki/exercise.html

"""

連立方程式を解くプログラム †
クラーメル法でもガウス法でもかまいません
"""

def gauss(M, a):
    d = len(M)
    if d != len(M[0]):
        return
    if d != len(a):
        return
    for i in range(0, d):
        p1 = M[i][i]
        if p1 == 0:
            for j in range(i+1, d):
                p2 = M[i][j]
                if p2 != 0:
                    z = M.pop(j)
                    M.insert(i, z)
                    break
            print("rank < {}".format(d))
            return
       
    for i in range(0, d - 1):
        pivot = M[i][i]
        if pivot != 0:
            for j in range(i,d):
                M[i][j] /= pivot
            a[i] /= pivot
            for j in range(i + 1, d):
                b = M[j][i]
                for k in range(i, d):
                    M[j][k] = M[j][k] - M[i][k] * b
                a[j] = a[j] - a[i] * b
   
    print(M, a)
    x = [0] * d
    for i in range(d-1, -1, -1):
        if i == d-1:
            x[i] = a[i] / M[i][i]
        else:
            x[i] = a[i]
            for j in range(i+1, d):
                x[i] -= x[j] * M[i][j]
    return (x)