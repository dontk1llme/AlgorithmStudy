#[BAEKJOON] 2564 경비원
# 왼쪽으로 한번, 오른쪽으로 한번 가서 더 작은 값이 최단거리 -> ㄴㄴㄴㄴ
# 절대값으로 구간 구하고 총 거리에서 구한 거리 빼면 반대거리겟죠? 
# (진짜 왼,오가 아니라 시각적으로... 0쪽으로 가는걸로...)

# 이동하는 법: 1,2라면 x, 3,4라면 y 거리 주기-> 이동하면 me=좌표 수정.
# 모든 케이스를 나눠서하면 너무 복잡할거같음... -> 함수쓰기
# 이게 초등부 문제?...... 미친거아냐?.................

#입력
x,y = map(int, input().split())
shopnum = int(input())
shop = [list(map(int, input().split())) for _ in range(shopnum)]
me = list(map(int, input().split())) #방향, 거리

#방향) 1: 북, 2: 남, 3:서, 4:동
for i in range(shopnum):
    if me[0]==1 or me[0]==2: #엥근데안되겟는데?
        







# https://otu165.tistory.com/2
# https://joanne.tistory.com/63
