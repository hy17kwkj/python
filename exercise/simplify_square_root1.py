# http://vipprog.net/wiki/exercise.html

"""
平方根を簡単な形にするプログラム †
例えば√8なら2√2にする。
√10000 (=100)まで列挙すること。
"""

import math
 
N = 10000
 
def div_square(x, maxN):
    for d in range(maxN, 0, -1):
        if x % (d**2) == 0:
            break
    return d, x // (d**2)
 
sqrtN = int(math.sqrt(N))
for i in range(1, N+1):
    d, r = div_square(i, sqrtN)
    print("√{} -> ".format(i), end="")
    if r == 1:
        print(d)
    elif d == 1:
        print("√{}".format(r))
    else:
        print("{}√{}".format(d, r))
