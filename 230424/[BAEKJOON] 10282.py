# boj 10282 해킹
# 다익스트라 사용. 
# 코드 https://velog.io/@hamfan524/%EB%B0%B1%EC%A4%80-10282%EB%B2%88-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Dijkstra
# https://pacific-ocean.tistory.com/292
# 다익스트라 https://m.blog.naver.com/ndb796/221234424646

# a,b,s 입력 시 a가 b를 의존한다는 표현; b->a


T = int(input())
for tc in range(1, T+1):
    n, d, c = map(int,input().split())
    lst = [list(map(int, input().split())) for _ in range(d)]
    ans = [0,0] # 감염되는 컴터 수, 마지막 컴터가 감염되기까지 걸리는 시간


    print(*ans)