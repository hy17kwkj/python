# http://vipprog.net/wiki/exercise.html

"""
スタック †
スタックを用いて後置記法で書かれた数式を計算するプログラムを書きなさい。
なお、入力は整数, +, -, *, /, %からなる式とし、出力は浮動小数点数にすること。
入力は下記のようにコマンドライン引数として受け取る形でも良い物とする。
$ ./a.out 1 2 + 3 * 4 5 + -
"""

expr = input("expr >>= ")
e = list(expr.strip().split(" "))
stack = []
expr_len = len(e)
n = 0
res = 0
while n < expr_len:
    print(e[n], stack)
    if e[n] in list("+-*/%"):
        op2 = stack.pop()
        op1 = stack.pop()
        if e[n] == "+":
            res = op1 + op2
        elif e[n] == "-":
            res = op1 - op2
        elif e[n] == "*":
            res = op1 * op2
        elif e[n] == "/":
            res = op1 / op2
        elif e[n] == "%":
            res = op1 % op2
        stack.append(res)
    else:
        stack.append(float(e[n]))
    n += 1
 
print(stack.pop())
