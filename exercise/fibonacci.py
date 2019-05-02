# フィボナッチ数(1,1,2,3,5,8,13,...)を2**31より小さい範囲まで表示する。

def fib(n):
    f0, f1, f2 = 1, 1, 2
    print(f0, f1, f2, end=" ")
    while True:
        f0, f1, f2 = f1, f2, f1+f2
        if f2 > n:
            break
        print(f2, end=" ")

fib(2**32-1)

# 無限にフィボナッチ級数を返し続けるgenerator。

def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b

for n in fibonacci():
    if n > 2**32-1:
        break
    print(n, end=" ")
