# 2つの自然数の最大公約数を求める（ユークリッドの互除法）

def gcd(a, b):
    if a < b:
        a, b = b, a
    while True:
        r = a % b
        if r == 0:
            break
        a, b = b, r
    return (b)
