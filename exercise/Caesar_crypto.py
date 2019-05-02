# http://vipprog.net/wiki/exercise.html

"""
Caesar暗号解読 †
Caesar暗号を解読するプログラムを作り,暗号を解読してください。
暗号鍵（何文字ずらすか）は不明ですが、文字列に"person"が含まれることがわかっています。
ご利用ください。 Caesar暗号についてはシーザー暗号-wikipediaを参照してください

"""

text_prev = "qdq-gi.q-a ziatmxxitmdqibtqi-ustbi ri.qmoqrcxi.qbubu zir -ibtqi-qp-qaai ripmymsqkir -ibtqi-qy dmxi ri.cnxuoi rruoumxakir -ibtqiqzmobyqzbkii-q.qmxi -imyqzpyqzbi rixmeaki -puzmzoqai -i-qscxmbu zaimzpir -i btq-iymbbq-a;iz -iatmxximzgi.q-a zinqiuzimzgiemgipuao-uyuzmbqpimsmuzabir -ia. za -uzsiacotiimi.qbubu zj"

moji = "abcdefghijklmnopqrstuvwxyz .,-"
while text_prev.find("person") < 0:
    text = ""
    for i in range(0, len(text_prev)):
        c = text_prev[i]
        j = moji.find(c) + 1
        if j >= len(moji):
            j = 0
        text += moji[j]
    text_prev = text
print(text_prev)
