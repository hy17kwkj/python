# http://vipprog.net/wiki/exercise.html

"""
数当てゲーム その２(Hit&Blow) †
これはｎ桁の数を探すゲームです。適当な数を入れると桁も数字もあっていれば
「Hit」としその個数が、数字はあっているが桁が異なっていれば「Blow」として
その個数が出力されます。それを繰り返すことで答えを探すことができます。
このゲームを作成しなさい。答えの数は乱数を使って毎回別の答えを用意しましょう。
具体的には
正解が1234だとして
4321　と入力　4blow
1245　と入力　2hit　1blow
なおルール上4422などのゾロ目の正解は出ないようにしましょう。
また、先頭が0だとn桁の数字じゃなくなるのでせっかくなので0は発生させないようにしましょう。
"""
 
a = list("123456789")
random.shuffle(a)
ans = a[0:4]
 
def hit(ans, you):
    h = 0
    for i in range(0, 4):
        if ans[i] == you[i]:
            h += 1
    return (h)
   
def blow(ans, you):
    b = 0
    for i in range(0, 4):
        if you[i] in ans and you[i] != ans[i]:
            b += 1
    return (b)
   
while True:
    while True:
        you = input("4桁の数を入力してください >> ")
        if 1234 <= int(you) <= 9876:
            break
    h = hit(ans, you)
    if h == 4:
        print("正解です")
        break
    b = blow(ans, you)
    print("hit {}, blow {}".format(h, b))
