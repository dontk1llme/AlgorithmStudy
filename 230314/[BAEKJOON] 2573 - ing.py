# boj 2573 빙산

N,M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
nlst = []
for i in range(N): #깊은 복사 -> 독립시행 보장
    nlst.append(lst[i][:])

dx = [-1,1,0,0]
dy = [0,0,-1,1]
year = 0
cnt = 1
while cnt<2:
    # 빙산 줄이기
    for i in range(N):
        for j in range(M):
            ocean = 0
            for k in range(4):
                nx = i+dx[k]
                ny = j+dy[k]

                if 0<=nx<N and 0<=ny<M:
                    if lst[nx][ny]==0:
                        ocean+=1
            nlst[i][j]-=ocean
            if nlst[i][j]<0: nlst[i][j]=0
    lst = nlst
    year+=1

    # 몇 덩이인지 확인하기 (1덩이가 아니면 year 출력)
    for i in range(N):
        for j in range(M):
            for k in range(4):
                nx = i+dx[k]
                ny = j+dy[k]
                if 0<=nx<N and 0<=ny<M:
                    if lst[nx][ny]==0:
