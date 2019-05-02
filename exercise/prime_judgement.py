# http://vipprog.net/wiki/exercise.html

"""
素数判定 †
与えられた数が素数かどうか調べる
あるいは与えられた数までの素数を列挙する
"""

import numpy as np
 
n = int(input("n= >> "))
sqrtn = int(np.sqrt(n))
sieve = np.zeros(sqrtn + 1)
sieve[0] = sieve[1] = 1
for i in range(2, sqrtn + 1):
    c = i * 2
    while c <= sqrtn:
        sieve[c] = 1
        c += i
 
isprime = True
for i in range(2, sqrtn + 1):
    if sieve[i] == 0:
        if n % i == 0:
            isprime = False
            break
 
if isprime == True:
    print("%d is prime." % n)
else:
    print("%d is not prime." % n)
