# AOJ 1001
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1001

import sys

def parse_btree(s):
    l = r = -1
    paren = 0
    comma = -1
    if s == "(,)":
        return (["node"])
    if s == "":
        return (["None"])
    for i in range(len(s)):
        c = s[i]
        if c == "(":
            paren += 1
            if paren == 1 and r < 0:
                l = i
        elif c == "," and paren == 1:
            r = i
        elif c == ")":
            paren -= 1
   
    return ([parse_btree(s[l + 1:r]), parse_btree(s[r + 1:-1])])
 
def deparse_btree(bt):
    if bt == ["None"]:
        return ("")
    elif bt == ["node"]:
        return ("(,)")
    else:
        return ("(" + deparse_btree(bt[0]) + "," + deparse_btree(bt[1]) + ")")
 
def intersection_btree(s, t):
    print("s=", s)
    print("t=", t)
    if s == ["node"] and t != ["None"]:
        return (["node"])
    elif s != ["None"] and t == ["node"]:
        return (["node"])
    elif s == ["None"] or t == ["None"]:
        return (["None"])
    return [intersection_btree(s[0], t[0]), intersection_btree(s[1], t[1])]
 
def union_btree(s, t):
#    print("s=", s)
#    print("t=", t)
    if s == ["node"]:
        if t != ["None"]:
           return (t)
        else:
            return (["node"])
    elif s == ["None"]:
        if t != ["None"]:
            return (t)
        else:
            return (["None"])
    if t == ["node"]:
        if s != ["None"]:
            return (s)
        else:
            return (["node"])
    elif t == ["None"]:
        if s != ["None"]:
            return (s)
        else:
            return (["None"])
    return [union_btree(s[0], t[0]), union_btree(s[1], t[1])]
 
f = open("python\input_1001.txt")
for line in f:
    s = line.strip().split()
    a = parse_btree(s[1])
    b = parse_btree(s[2])
    if s[0] == 'i':
        c = intersection_btree(a, b)
        print(c)
        print(deparse_btree(c))
    elif s[0] == 'u':
        print(deparse_btree(union_btree(a, b)))
f.close()
