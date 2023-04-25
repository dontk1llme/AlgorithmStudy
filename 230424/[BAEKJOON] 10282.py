# boj 10282 해킹
# 다익스트라 사용. 
# 코드 https://velog.io/@hamfan524/%EB%B0%B1%EC%A4%80-10282%EB%B2%88-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Dijkstra
# https://pacific-ocean.tistory.com/292
# 다익스트라 https://m.blog.naver.com/ndb796/221234424646

# a,b,s 입력 시 a가 b를 의존한다는 표현; b->a

from heapq import heappush, heappop
import sys
input = sys.stdin.readline
inf = 100000000
def dijkstra(start): #최단 시간 구하기
    heap = []
    heappush(heap, [0, start])
    dp = [inf for i in range(n + 1)]
    dp[start] = 0
    while heap:
        we, nu = heappop(heap)
        for ne, nw in lst[nu]:
            wei = we + nw
            if dp[ne] > wei:
                dp[ne] = wei
                heappush(heap, [wei, ne])
    return dp

T = int(input())
for tc in range(1, T+1):
    n, d, start = map(int,input().split())
    lst = [[] for i in range(n + 1)]
    for i in range(d): #그래프 생성
        a, b, c = map(int, input().split())
        lst[b].append([a, c])
    dp = dijkstra(start) #시작점에서 다익스트라 진행
    max_dp = 0
    cnt = 0
    # print(dp)
    for i in dp:
        if i != inf: #시간 중 가장 큰 값과 컴터 개수 출력
            if max_dp < i:
                max_dp = i
            cnt += 1
    print(cnt, max_dp)