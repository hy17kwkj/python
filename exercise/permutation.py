# 文字候補'python'からn文字の文字列を生成する(重複なしの場合)

def perm(n, m):
    if m<1:
        yield()
    else:
        for r in perm(n, m-1):
            for x in xrange(n):
                if x not in r:
                    yield r + (x,)

def create_word_list_p(n, s):
    return [''.join(s[i] for i in t) for t in perm(len(s), n)]
 
create_word_list_p(3, 'python')
