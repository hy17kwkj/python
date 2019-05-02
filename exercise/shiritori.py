# http://vipprog.net/wiki/exercise.html


"""
英単語しりとりプログラム †
あらかじめ用意した「辞書ファイル」の内容に基づいて、ユーザーとしりとりをする対話プログラム。
辞書ファイルのフォーマットは、キャリッジリターンで区切られた半角英字のみのテキスファイルとする。
"""

import re
 
outf = open("words.txt", "w")
with open("words_org.txt") as f:
    for l in f:
        a = re.split(r"[0-9 ()-.,\n\[\]]", l.strip(" \n"))
        a = [x for x in a if x != ""]
#        print(a)
        for w in a:
            print(w.lower(), file=outf)
outf.close()

import random
 
words = []
shiritori = []
 
def read_words():
    dic = []
    with open("words.txt") as f:
        for w in f:
            w = w.strip()
            dic.append(w)
    return (dic)
 
def search_words(w, letter, dic):
    for d in dic:
        if d == w and letter == w[0]:
            return (True)
    return (False)
 
def search_words_head(w, dic, shiritori):
    for d in dic:
        if d[0] == w[-1] and not(d in shiritori):
            return (d)
    return (None)
 
def is_used(w, shiritori):
    if w in shiritori:
        return (shiritori.index(w) + 1)
    else:
        return (False)


import random
import sys
 
shiritori = []
senkou = random.randint(0, 1)
words = read_words()
 
count = 0
while True:
    count += 1
    #print("count = ", count, senkou)
    if count == 1:
        if senkou == 0:  # comが先攻
            w = random.choice(words)
            print("わたし:", w)
            shiritori.append(w)
        else:
            letter = random.choice("abcdefghijklmnopqrstuvwxyz")
            print("最初の文字: ", letter)
            w = input("あなた >> ")
            while search_words(w, letter, words) == False:
                print("その単語は辞書にありません。")
                w = input("あなた >> ")
            shiritori.append(w)
    else:
        if (count + senkou) % 2 == 1:  # comの番
            d = search_words_head(w, words, shiritori)
            if d == None:
                print("まいりました。あなたの勝ちです。")
                sys.exit()
            else:
                print("わたし:", d)
                w = d
                shiritori.append(w)
        else:
            letter = w[-1]
            w = input("あなた >> ")
            while True:
                if search_words(w, letter, words) == False:
                    print("その単語は辞書にありません。")
                else:
                    u = is_used(w, shiritori)
                    if u != False:
                        print("その単語は%d回目に" % u, ("あなたが" if (u + senkou) % 2 == 0 else "わたしが"), \
                              "使用しています。" \
                              "わたしの勝ちです。" \
                              "今回のしりとりでは %d 個の単語を使用しました。" %len(shiritori))
                        sys.exit()
                    else:
                        shiritori.append(w)
                        break
                w = input("あなた >> ")
				