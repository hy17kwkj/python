#!/usr/local/bin/python3
# coding: UTF-8
"""
    PL/SQL から非互換構文を抽出するツール

    引数にPL/SQLソースファイル名を指定し、結果を標準出力に出力する。

    usage: python plsql_syntaxext.py  (inputfile)
"""


import sys
import re

# コマンドライン引数
args = sys.argv

# 入力ファイル名
if len(args) < 1:
    print("入力ファイル名を指定してください。")
    sys.exit()
filename = args[1]

# SQL終了フラグ。セミコロンが来るとtrueになる
sqlend = False
# ブロックコメントの内部か？
blkcomment = False
# トークン
token = ""
# トークンを格納するキュー
queue = []

# 区切り記号 (delim1が1文字、delim2が2文字)
delim1 = [",", "=", "(", ")"]
delim2 = [":=", ">=", "<=", "!=", "=>"]

# 行番号
ln = 1

# 難易度を示す定数
EASY = 0
MEDIUM = 1
HARD = 2
difficulty = ["低", "中", "高"]

### 以下は非互換構文チェックで使用
# 定義されたユーザ例外の名称
user_exception_name = []
# カーソル変数の名称
cursor_variable_name = []

# Oracleの事前定義例外の名称
oracle_exception_name = [
    "ACCESS_INTO_NULL",
    "CASE_NOT_FOUND",
    "COLLECTION_IS_NULL",
    "CURSOR_ALREADY_OPEN",
    "DUP_VAL_ON_INDEX",
    "INVALID_CURSOR",
    "INVALID_NUMBER",
    "LOGIN_DENIED",
    "NO_DATA_FOUND",
    "NO_DATA_NEEDED",
    "NOT_LOGGED_ON",
    "PROGRAM_ERROR",
    "ROWTYPE_MISMATCH",
    "SELF_IS_NULL",
    "SUBSCRIPT_BEYOND_COUNT",
    "SUBSCRIPT_OUTSIDE_LIMIT",
    "SYS_INVALID_ROWID",
    "STORAGE_ERROR",
    "TIMEOUT_ON_RESOURCE",
    "TOO_MANY_ROWS",
    "USERENV_COMMITSCN_ERROR",
    "TRANSACTION_BACKED_OUT",
    "VALUE_ERROR",
    "ZERO_DIVIDE",
    "OTHERS"
]


### トークンをキューに追加する
def add_token():
    global token
    global ln
    if token != "":
        queue.append((token, ln))
        token = ""

### キューからキーワードを探す
# 見つかったらインデックスと行番号を返す
# 見つからなかったら -1と0を返す
#
#   キーワードは全て小文字で記述する。
def search_keyword(q, kw):
    for n, tl in enumerate(q):
        t, l = tl
        if t == kw:
            return n, l
    else:
        return -1, 0

### キューから正規表現パターンを探す
# 見つかったらインデックスと行番号を返す
# 見つからなかったら -1と0を返す
#
#   キーワードは全て小文字で記述する。
def search_keyword_regex(q, pattern):
    repattern = re.compile(pattern)
    for n, tl in enumerate(q):
        t, l = tl
        result = repattern.match(t)
        if result:
            return n, l
    else:
        return -1, 0

### 非互換構文チェック内容を出力する
# 引数:
#   m, n:   非互換の番号
#   d:      難易度
#   msg:    メッセージ
#   fn:     ファイル名
#   l:      行番号
def output_log(m, n, d, msg, fn, l):
    print('PLSQL-{:03d}-{:03d},{},"{}",{},"{}"'.format(m, n, difficulty[d], fn, l, msg))


### 非互換構文チェック
# 引数:
#   q:  トークンを格納したキュー
#   fn: ファイル名
def check_syntax(q, fn):
    # キューの中のトークンを全て小文字に
    q1 = [(t.lower(), l) for t, l in q]
    # キューから行番号の情報を削除
    q2 = [t for t, l in q1]

    # カーソルの宣言
    j, l = search_keyword(q1, "cursor")
    if j != -1:
        output_log(1, 1, EASY, "CURSOR定義文は非互換です。カーソル名とCURSOR句を入れ替えます。", fn, l)
        if j + 1 < len(q):
            cursor_variable_name.append(q2[j + 1])
        # default句の存在
        if "defalut" in q2[j + 1:]:
            output_log(1, 2, EASY, "カーソルパラメータにDEFAULT句を記述することはできません。", fn, l)
        # REF CURSOR型
        if j > 0 and q2[j - 1] == "ref":
            output_log(1, 3, EASY, "REF CURSOR型はサポート外です。refcursor型に書き換えます。", fn, l)

    # EXCEPTION型の変数宣言
    j, l = search_keyword(q1, "exception")
    if len(q) == 2 and j == 1:
        output_log(2, 1, EASY, "PL/pgSQLはEXCEPTION型の変数を定義できません。", fn, l)
        user_exception_name.append(q2[0])
    # 例外ハンドラの記述
    if j == 0 and q2[1] == "when":
        output_log(2, 2, HARD,  "PL/pgSQLは例外ハンドラの記述に互換性がありません。とくにPL/pgSQLでは例外の捕捉時にBEGIN句以降の変更を暗黙的にロールバックします。", fn, l)

        # Oracleの事前定義例外の名称
        # 非互換の枝番は3から27を順に付与する
        for n, en in enumerate(oracle_exception_name):
            if q2[2] == en.lower():
                output_log(2, 3 + n, MEDIUM, "Oracleの事前定義例外の名称" + en + "はPL/pgSQLへの移行時に書き換えを必要とします。", fn, l)

    # RAISE文による例外送出
    j, l = search_keyword(q1, "raise")
    if j != -1 and j + 1 < len(q) and q2[j + 1] in user_exception_name:
        output_log(3, 1, EASY, "PL/pgSQLはユーザ定義例外の送出の記述が異なります。", fn, l)

    # トランザクション制御
    j, l = search_keyword(q1, "commit")
    if j != -1:
        output_log(4, 1, HARD, "プロシージャでのトランザクション制御(COMMIT)はPostgreSQL11から可能ですが、Oracleと同じ挙動になる保証はありません。検証が必要です。", fn, l)

    # トランザクション制御
    j, l = search_keyword(q1, "rollback")
    if j != -1:
        output_log(4, 2, HARD, "プロシージャでのトランザクション制御(ROLLBACK)はPostgreSQL11から可能ですが、Oracleと同じ挙動になる保証はありません。検証が必要です。", fn, l)

    # TYPE宣言で %TYPE を用いること
    j, l = search_keyword(q1, "type")
    if j != -1 and q2[j + 2] == "is":
        for t in q2[j + 3:]:
            if t[-5:] == "%type":
                output_log(5, 1, EASY, "TYPE宣言で%TYPEを使った型の指定はサポート外です。実際の型名を記述してください。", fn, l)
                break
        if q2[j + 3] == "table" and q2[j + 4] == "of":
            output_log(5, 2, EASY, "TYPE ... IS TABLE OF宣言はサポート外です。", fn, l)
        if q2[j + 3] == "record":
            output_log(5, 3, EASY, "TYPE ... IS RECORD宣言はサポート外です。", fn, l)

    # 引数のin、out、inout属性の記述位置
    j, l = search_keyword(q1, "procedure")
    j0 = -1
    if j == -1:
        j, l = search_keyword(q1, "function")
        j0 = j
    if j != -1:
        if "in" in q2[j + 1:] or "out" in q2[j + 1:] or "inout" in q2[j + 1:]:
            output_log(6, 1, EASY, "引数のin、out、inout属性の記述位置がPL/pgSQLでは異なります。", fn, l)
    if j0 != -1:
        if "out" in q2[j0 + 1:]:
            output_log(6, 2, EASY, "OUT属性の引数を持つ関数では、返り値をOUT属性の引数として追加します。", fn, l)


    # カーソル変数に %rowtype を後ろにつける記述
    j, l = search_keyword(q1, "%rowtype")
    if j != -1 and len(q) == 3:
        for csr in cursor_variable_name:
           if csr == q2[j - 1]:
               output_log(7, 1, EASY, "カーソル変数に%ROWTYPEを付与する記述はできません。RECORD型を使用してください。", fn, l)
               break
    for csr in cursor_variable_name:
        j, l = search_keyword(q1, csr + "%rowtype")
        if j != -1:
           output_log(7, 1, EASY, "カーソル変数に%ROWTYPEを付与する記述はできません。RECORD型を使用してください。", fn, l)
           break

    # %FOUND, %NOTFOUND
    j, l = search_keyword_regex(q1, r".*%found")
    if j != -1:
        output_log(8, 1, EASY, "%FOUND変数はサポート外です。組み込み変数FOUNDを用います。", fn, l)
    j, l = search_keyword_regex(q1, ".*%notfound")
    if j != -1:
        output_log(8, 2, EASY, "%NOTFOUND変数はサポート外です。組み込み変数FOUNDを用います。", fn, l)

    # %ISOPEN
    j, l = search_keyword_regex(q1, r".*%isopen")
    if j != -1:
        output_log(9, 1, MEDIUM, "%ISOPEN変数はサポート外です。カーソルがオープンされているかを知る手段はありません。確実にカーソルを閉じるよう処理を検討します。", fn, l)

    # .DELETE
    j, l = search_keyword_regex(q1, r".*\.\s*delete")
    if j != -1:
        output_log(10, 1, EASY, "配列をすべて削除するDELETEはサポート外です。代わりに要素数0の配列を代入します。", fn, l)

    # .COUNT
    j, l = search_keyword_regex(q1, r".*\.\s*count")
    if j != -1:
        output_log(11, 1, EASY, "配列の要素数を返すCOUNTはサポート外です。array_length()関数で書き換えます。", fn, l)

    # UTL_FILE
    j, l = search_keyword_regex(q1, r"utl_file\s*\..*")
    if j != -1:
        output_log(12, 1, EASY,  "UTL_FILEパッケージはサポート外です。パッケージ内の一部の関数はorafceを用いることで利用可能です。", fn, l)

    # EXECUTE IMMEDIATE
    j, l = search_keyword(q1, "execute")
    if j != -1 and q2[j + 1] == "immediate":
        output_log(13, 1, EASY, "EXECUTE IMMEDIATE文はサポート外です。PERFORM文もしくはEXECUTE文で書き換えます。", fn, l)

    # GOTO
    j, l = search_keyword(q1, "goto")
    if j != -1:
        output_log(14, 1, MEDIUM, "GOTO文はサポート外です。", fn, l)

    # 自律型トランザクション
    j, l = search_keyword(q1, "pragma")
    if j != -1 and q2[j + 1] == "autonomous_transaction":
        output_log(15, 1, MEDIUM, "自律型トランザクションはサポート外です。dblinkで書き換える方法があります。", fn, l)

    # FETCH BULK
    j, l = search_keyword(q1, "fetch")
    if j != -1 and q2[j + 2:j + 4] == ["bulk", "collect"]:
        output_log(16, 1, EASY, "FETCH ... BULK COLLECTはサポート外です。", fn, l)

    # FORALL
    j, l = search_keyword(q1, "forall")
    if j != -1:
        output_log(17, 1, EASY, "FORALL文はサポート外です。FOR文で書き換えますが、性能が落ちるかもしれません。", fn, l)

    # FOR ... IN REVERSE
    j, l = search_keyword(q1, "for")
    if j != -1 and j + 3 < len(q) and q2[j + 2] == "in" and q2[j + 3] == "reverse":
        output_log(18, 1, EASY, "FOR ... IN REVERSEループの上限値と下限値の記述順が逆になります。", fn, l)

    # PUT_LINE()関数
    j, l = search_keyword_regex(q1, r"dbms_output\s*\.\s*put_line")
    if j != -1:
        output_log(19, 1, EASY, "DBMS_OUTPUT.PUT_LINE()関数はサポート外です。orafceを用いることで利用可能です。", fn, l)

    # DBMS_DATAPUMPモジュール
    j, l = search_keyword_regex(q1, r".*dbms_datapump.ku$_file_type_dump_file.*")
    if j != -1:
        output_log(20, 1, HARD, "DBMS_DATAPUMP.KU$_FILE_TYPE_DUMP_FILEモジュールはサポート外です。", fn, l)
    j, l = search_keyword_regex(q1, r".*dbms_datapump.add_file.*")
    if j != -1:
        output_log(20, 2, HARD, "DBMS_DATAPUMP.ADD_FILEモジュールはサポート外です。", fn, l)
    j, l = search_keyword_regex(q1, r".*dbms_datapump.ku$_file_type_log_file.*")
    if j != -1:
        output_log(20, 3, HARD, "DBMS_DATAPUMP.KU$_FILE_TYPE_LOG_FILEモジュールはサポート外です。", fn, l)
    j, l = search_keyword_regex(q1, r".*dbms_datapump.detach.*")
    if j != -1:
        output_log(20, 4, HARD, "DBMS_DATAPUMP.DETACHモジュールはサポート外です。", fn, l)
    j, l = search_keyword_regex(q1, r".*dbms_datapump.metadata_filter.*")
    if j != -1:
        output_log(20, 5, HARD, "DBMS_DATAPUMP.METADATA_FILTERモジュールはサポート外です。", fn, l)
    j, l = search_keyword_regex(q1, r".*dbms_datapump.open.*")
    if j != -1:
        output_log(20, 6, HARD, "DBMS_DATAPUMP.OPENモジュールはサポート外です。", fn, l)
    j, l = search_keyword_regex(q1, r".*dbms_datapump.set_parameter.*")
    if j != -1:
        output_log(20, 7, HARD, "DBMS_DATAPUMP.SET_PARAMETERモジュールはサポート外です。", fn, l)
    j, l = search_keyword_regex(q1, r".*dbms_datapump.start_job.*")
    if j != -1:
        output_log(20, 8, HARD, "DBMS_DATAPUMP.START_JOBモジュールはサポート外です。", fn, l)
    j, l = search_keyword_regex(q1, r".*dbms_datapump.stop_job.*")
    if j != -1:
        output_log(20, 9, HARD, "DBMS_DATAPUMP.STOP_JOBモジュールはサポート外です。", fn, l)

    # CREATE PACKAGE
    j, l = search_keyword(q1, "package")
    if j != -1 or (j >= 1 and q2[j - 1] == "create") or \
        (j >= 3 and q2[j - 3:j] == ["create", "or", "replace"]):
        output_log(21, 1, MEDIUM, "パッケージはサポート外です。パッケージ変数を使っている場合は移行を必要とします。", fn, l)   

    # CREATE FUNCTION
    j, l = search_keyword(q1, "function")
    if j != -1 or (j >= 1 and q2[j - 1] == "create") or \
        (j >= 3 and q2[j - 3:j] == ["create", "or", "replace"]):
        output_log(22, 1, EASY, "関数定義の書式はPL/SQLとは異なります。PL/pgSQLの構文に従って書き換えます。", fn, l)

    # CREATE PROCEDURE
    j, l = search_keyword(q1, "procedure")
    if j != -1 or (j >= 1 and q2[j - 1] == "create") or \
        (j >= 3 and q2[j - 3:j] == ["create", "or", "replace"]):
        output_log(23, 1, EASY, "プロシージャはPostgreSQL11以降でサポートしますが書式はPL/SQLとは異なります。PostgreSQL10以前であれば関数で書き換えます。", fn, l)   

    # SQL%ROWCOUNT
    j, l = search_keyword(q1, "sql%rowcount")
    if j != -1:
        output_log(24, 1, EASY, "SQL%ROWCOUNTはサポート外です。GET DIAGNOSTICS文とROW_COUNT変数で書き換えます。", fn, l)

    # データ型
    # 番号の枝番は db_syntax_diff に従うものとする。
    j, l = search_keyword(q1, "char")
    if j != -1:
        output_log(25, 1, EASY, "CHAR型が使用されています。このまま移行する場合、データが文字単位で扱われますので注意が必要です。また、CHAR型とVARCHAR型との比較を行う場合、Oracleと異なり空白埋め比較が行われますので注意が必要です。この場合、VARCHAR型をTEXT型に変更することで非空白埋め比較が行われます。", fn, l)
    j, l = search_keyword(q1, "nchar")
    if j != -1:
        output_log(25, 2, EASY, "NCHAR型はサポートされていません。CHAR型に変更することで対処可能ですが、各国語キャラクタ・セットの種別に関わらずデータが文字単位で扱われますので注意が必要です。また、CHAR型とVARCHAR型との比較を行う場合、Oracleと異なり空白埋め比較が行われますので注意が必要です。この場合、VARCHAR型をTEXT型に変更することで非空白埋め比較が行われます。", fn, l)
    j, l = search_keyword(q1, "nvarchar2")
    if j != -1:
        output_log(25, 3, EASY, "NVARCHAR2型はサポートされていません。VARCHAR型に変更することで対処可能ですが、各国語キャラクタ・セットの種別に関わらずデータが文字単位で扱われますので注意が必要です。また、CHAR型とVARCHAR型との比較を行う場合、Oracleと異なり空白埋め比較が行われますので注意が必要です。この場合、VARCHAR型をTEXT型に変更することで非空白埋め比較が行われます。", fn, l)
    j, l = search_keyword(q1, "varchar2")
    if j != -1:
        output_log(25, 4, EASY, "VARCHAR2型はサポートされていません。TEXT型に変更することで対処可能ですが、データは文字単位で扱われますので注意が必要です。", fn, l)
    j, l = search_keyword(q1, "varchar")
    if j != -1:
        output_log(25, 5, EASY, "VARCHAR型が使用されています。このまま移行する場合、データが文字単位で扱われますので注意が必要です。また、CHAR型とVARCHAR型との比較を行う場合、Oracleと異なり空白埋め比較が行われますので注意が必要です。この場合、VARCHAR型をTEXT型に変更することで非空白埋め比較が行われます。", fn, l)
    j, l = search_keyword(q1, "number")
    if j != -1:
        output_log(25, 6, EASY, "NUMBER型はサポートされていません。NUMERIC型に変更することで対応可能ですが、位取りの値に、負数および、精度より大きい値は指定できませんので注意が必要です。また、NUMERIC型は性能上問題となる場合がありますので、厳密に精度を求める必要がない場合はREAL型やINTEGER型など、他の型の利用を検討してください。", fn, l)
    j, l = search_keyword(q1, "date")
    if j != -1:
        output_log(25, 8, EASY, "DATE型が使用されています。時刻情報は格納されないので注意が必要です。時刻情報を格納する場合はTIMESTAMP型の利用を検討してください。", fn, l)
    j, l = search_keyword(q1, "raw")
    if j != -1:
        output_log(25, 14, EASY, "RAW型はサポートされていません。bytea型への移行を検討します。", fn, l)




### 1行ずつ読み取る
fo = open(filename, "r")
line = fo.readline()
while line:

    length = len(line)

    # ラインコメントの内部か？
    lincomment = False
    # リテラルの内部か？
    literal = False

    # 各行を1文字ずつ調べる
    i = 0
    while i < length:

        # 空白の読み飛ばし
        if line[i] in " \t\n":
            add_token()

        # 区切り記号
        elif line[i] in delim1:
            add_token()
            token = line[i]
            add_token()
        elif line[i:i+2] in delim2:
            add_token()
            token = line[i:i+2]
            add_token()
            i += 1

        # ブロックコメントの終端？
        elif line[i:i+2] == "*/" and blkcomment == True:
            blkcomment = False
            i += 1

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
            # リテラルの内部か
            elif line[i] == "'" and literal == False:
                literal = True
                token = "'"

            # SQLの終端か
            elif line[i] == ";":
                sqlend = True
            else:
                token += line[i]


        elif literal == True:
            token += line[i]
            # リテラルの外部か
            if line[i] == "'" and literal == True:
                literal = False
                add_token()

        #if token.lower() == "is":
        #    sqlend = True

        # 文の終わり
        if sqlend == True:
            sqlend = False
            add_token()
            # 非互換構文チェック
            check_syntax(queue, filename)

            # 文が終わるのでトークンのキューをクリアする
            #print(queue)
            queue = []

        # 次の文字を見る
        i += 1

     # 行番号をインクリメント
    ln += 1
    line = fo.readline()

fo.close()