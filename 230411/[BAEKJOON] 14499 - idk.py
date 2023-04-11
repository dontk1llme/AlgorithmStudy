# boj 14499 주사위 굴리기
# 시뮬레이션
# 먼소리임?

#   2
# 4 1 3
#   5
#   6

N,M,x,y,K = map(int,input().split()) #세로, 가로, 좌표, 명령
lst = list(map(int, input().split()) for _ in range(N)) #
klist = list(map(int,input().split()))