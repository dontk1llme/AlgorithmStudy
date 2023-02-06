#[BAEKJOON] 2564 경비원
# 왼쪽으로 한번, 오른쪽으로 한번 가서 더 작은 값이 최단거리
# (진짜 왼,오가 아니라 시각적으로... 0쪽으로 가는걸로...)
# 이동하는 법: 1,2라면 x, 3,4라면 y 거리 주기-> 이동하면 me=좌표 수정.
# 모든 케이스를 나눠서하면 너무 복잡할거같음... -> 함수쓰기
# 이게 초등부 문제?...... 미친거아냐?.................

#입력
x,y = map(int, input().split())
shopnum = int(input())
shop = [list(map(int, input().split())) for _ in range(shopnum)]
me = list(map(int, input().split()))


#상황별 판단은 함수로 하자................
def where(lst):
    for i in range







# https://otu165.tistory.com/2
# https://joanne.tistory.com/63
