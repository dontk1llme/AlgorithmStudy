# boj 3055 탈출
# D -> S. 최단시간 -> BFS
# 물 채우고 고슴도치 이동하고 시간 +하기
# https://velog.io/@ms269/%EB%B0%B1%EC%A4%80-3055-%ED%83%88%EC%B6%9C-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python
# https://kyun2da.github.io/2020/09/22/escape/
# https://sinsomi.tistory.com/entry/%EB%B0%B1%EC%A4%80-Python-3055%EB%B2%88-%ED%83%88%EC%B6%9C-%EC%B4%88%EC%BD%94%EB%8D%94
# https://campkim.tistory.com/16

dlst= [(0,1), (1,0), (-1,0), (0,-1)]
def bfs(x,y):
    if lst[i][j]=='*':




R, C = map(int,input().split())
lst = [list(map(str, input())) for _ in range(R)]
x,y = 0,0

for i in range(R): #시작점 찾기
    for j in range(C):
        if lst[i][j]=='D':
            x,y = i,j

cnt = 0 #tmpans
ans = 0
bfs(x,y)
if ans==0:
    print("KAKTUS")
else:
    print(ans)