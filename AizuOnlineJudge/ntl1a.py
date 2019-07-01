# AOJ NTL_1_A
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_A

import math

def primes(n):
    rn = int(math.sqrt(n))
    sieve = [1] * (rn + 1)
    for i in range(2, rn + 1):
        j = i * 2
        while j <= rn:
            sieve[j] = 0
            j += i
    p = [i for i in range(2, rn + 1) if sieve[i] == 1]
    return p

def factorize(n, p):
    out = ["{}:".format(n)]
    while n > 1:
        for q in p:
            if n % q == 0:
                out += [str(q)]
                n //= q
                break
        else:
            out += [str(n)]
            break
    print(" ".join(out))

line = input()
n = int(line)
p = primes(n)
factorize(n, p)
