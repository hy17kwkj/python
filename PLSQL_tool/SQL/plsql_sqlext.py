#!/usr/local/bin/python3
# coding: utf-8
"""
    PL/SQL から DML文を抽出するツール

    抽出したDML文を標準出力に出力する。

    usage: python plsql_sqlext.py < (inputfile)
"""


import sys

# SQL終了フラグ。セミコロンが来るとtrueになる
sqlend = False
# SQL開始フラグ。DML文が来るとtrueになる。
sqlstart = False
# ブロックコメントの内部か？
blkcomment = False
# 行番号
ln = 1

# 1行ずつ読み取る
for line in sys.stdin:

    # 行末の改行コードをカットする
    line = line.rstrip('\n')
    length = len(line)

    # ラインコメントの内部か？
    lincomment = False
    # リテラルの内部か？
    literal = False
    # 1つ手前の文字が空白か？
    blank = True

    # 各行を1文字ずつ調べる
    i = 0
    while i < length:
        #print(literal, line[i])

        # DML文の候補(注目位置から6文字分)
        cmd = line[i:i+6].lower()

        # 共通テーブル式か
        cte = line[i:i+4].lower()

        # ブロックコメントの終端？
        if line[i:i+2] == "*/" and blkcomment == True:
            blkcomment = False

        # コメントの内部であれば読み飛ばす
        elif blkcomment == True or lincomment == True:
            pass

        # リテラルの内部でなければ文字を調べる
        elif literal == False:
            # ラインコメント
            if line[i:i+2] == "--":
                lincomment = True
            # ブロックコメント
            elif line[i:i+2] == "/*":
                blkcomment = True
            # リテラルに入る
            elif line[i] == "'":
                literal = True

            # SQLの終端か
            elif line[i] == ";" and sqlstart == True:
                sqlend = True
                # print("ln = ", ln)

            # DML文かを調べ、SQL開始フラグを立てる
            # 2行下のANDはこれらのキーワードの手前が空白か？
            # 3行下のANDはこれらのキーワードの次が行末か空白であるか？
            elif (cmd == "select" or cmd == "update" or cmd == "insert" or cmd == "delete")\
                    and sqlstart == False \
                    and blank == True \
                    and (i + 6 == length \
                         or (i + 6 < length and line[i+6] == " ")):
                #print("-- 開始行番号 =", ln)
                print(" " * i, end="")
                sqlstart = True

            # 共通テーブル式か？
            elif cte == "with" and sqlstart == False and blank == True \
                    and (i + 4 == length or (i + 4 < length and line[i+4] == " ")):
                print(" " * i, end = "")
                sqlstart = True

        # リテラルの外部か
        else:
            if line[i] == "'":
                literal = False

        # SQL開始フラグが立っていればその文字を標準出力に出力
        if sqlstart == True:
            print(line[i], end="")
            # セミコロンが来る
            if sqlend == True:
                #print("")
                #print("-- 終了行番号 =", ln)
                sqlend = False
                sqlstart = False

        # 文字が空白か？
        blank = (line[i] == " " or line[i] == '\t')

        # 次の文字を見る
        i += 1

    # 改行する
    print("")

    # 行番号をインクリメント
    ln += 1