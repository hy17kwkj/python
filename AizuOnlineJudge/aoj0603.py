# AOJ0603
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0603

illu = []
n = 0

def findmax(begin, end):
    flag = illu[begin]
    l = 1
    maxlen = 1
    for i in range(begin + 1, end + 1):
        if illu[i] + flag == 1:
            l += 1
        else:
            if l > maxlen:
                maxlen = l
            l = 1
        flag = illu[i]
    return maxlen if maxlen > l else l

def find_alterseq():
    seq = []
    s = e = 0
    flag = illu[0]
    for i in range(1, n + 1):
        if illu[i] + flag != 1:
            seq.append([s, i - 1])
            s = i
        flag = illu[i]
    return seq

def reverse(s, e):
    for i in range(s, e + 1):
        illu[i] = 1 - illu[i]

def solve():
    alseq = find_alterseq()
    maxlen = 0
    alseq.insert(0, [0, 0])
    alseq.append([n, n])
    nindex = len(alseq)
    for i in range(1, nindex - 1):
        s, e = alseq[i]
        begin = alseq[i - 1][0]
        end = alseq[i + 1][1]
        if end - begin + 1 >= maxlen:
            reverse(s, e)
            l = findmax(begin, end)
            if l > maxlen:
                maxlen = l
            reverse(s, e)
    return maxlen

f = open("python\input_0603.txt")
line = f.readline()
#line = input()
n = int(line)
illu = list(map(int, list(f.readline().split())))
#illu = list(map(int, list(input().split())))
illu.append(999)
ans = solve()
print(ans)
