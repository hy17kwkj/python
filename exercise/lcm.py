# 2つの自然数の最小公倍数を求める。

def lcm(a, b):
    return (a * b / gcd(a, b))

lcm(12,18)
