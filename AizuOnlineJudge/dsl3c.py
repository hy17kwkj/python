# AOJ DSL_3_C
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_3_C

line = input()
N, Q = list(map(int, line.split()))
line = input()
arr = list(map(int, line.split()))
line = input()
query = list(map(int, line.split()))

def solve(query):
    ans = [0] * Q
    s = [0] * N
    for i in range(0, N):
        t = [ s[j - i] + arr[j] for j in range(i, N)]
        l = [ len([0 for b in t if b <= q]) for q in query]
#        l = [ len(list(filter(lambda x: x <= q, t ))) for q in query]
        ans = [a + b for a, b in zip(ans, l)]
        s = t
        #print(t)
    return ans

ans = solve(query)
print("\n".join(map(str, ans)))
