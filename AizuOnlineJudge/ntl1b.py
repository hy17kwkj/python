# AOJ NTL_1_B
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_B

MOD = 1000000007

def power(m, n):
    a = m
    ans = 1
    while n > 0:
        if n & 1:
            ans = ans * a % MOD
        n >>= 1
        a = a * a % MOD
    return ans

line = input()
m, n = list(map(int, line.split()))
print(power(m, n))
