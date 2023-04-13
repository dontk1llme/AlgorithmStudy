# boj 1717 집합의 표현
# union과 findparent 할수있는지 묻는것
# 언뜻 보면 쉬운 것 같은데 시간초과
# https://devlibrary00108.tistory.com/35  |   https://jrc-park.tistory.com/247
# https://velog.io/@myway00/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-289%EB%B2%88-%EB%B0%B1%EC%A4%80-%EB%B2%88
# 알고리즘 https://0x15.tistory.com/34

import sys #시간초과 방지용
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n,m = map(int,input().split())
sett = [i for i in range(n+1)] #하나하나 리스트로 안해줘도 ㄱㅊ

def unionn(a,b):
    a = findd(a)
    b = findd(b)
    if a>b:
        sett[a]=b
    else: sett[b]=a

def findd(u):
    if sett[u]==u:
        return u
    sett[u]=findd(sett[u])
    return sett[u]

for _ in range(m):
    c, a, b = map(int,input().split())
    if c:
        if findd(a)==findd(b):
            print("YES")
        else:
            print("NO")
    else: unionn(a,b)



# for i in range(m):
#     c, a, b = map(int,input().split())
#     if c==0: #합집합
#         tmp = []
#         for i in range(len(sett)):
#             if a in sett[i] or b in sett[i]:
#                 tmp.append(sett.pop(i))
#                 print(tmp)
#                 print(i)


