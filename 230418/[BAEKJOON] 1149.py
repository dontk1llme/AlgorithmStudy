# boj 1149
# 너무 어렵게 생각하지 않기... https://namhandong.tistory.com/131
# 현재 집에서 각각 색을 칠했을 때의 가장 적은 비용을 저장해서 재사용하는 것을 중점으로!
# ㄴ https://myjamong.tistory.com/309
# 1번 집 색 != 2번 집 색
# n번 집 색 != n-1번 집 색
# i(2<=i<=N-1) 집 색 != i-1, i+1번 집 색


N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    #빨간집
    lst[i][0] += min(lst[i-1][1], lst[i-1][2])
    #초록집
    lst[i][1] += min(lst[i-1][0], lst[i-1][2])
    #파랑집
    lst[i][2] += min(lst[i-1][0], lst[i-1][1])

ans = min(lst[N-1])
print(ans)