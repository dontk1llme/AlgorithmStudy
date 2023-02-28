# 2206 벽 부수고 이동하기
# 하나 부숴도됨. 최단거리 출력. 불가능이면 -1
# 엥 3차원배열 쓰라고요?........ 뭔.. 뭔소링미
# https://hongcoding.tistory.com/18

from collections import deque

#상하좌우
d = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs(r,c,N,M):
    q = deque()
    q.append((r,c))
    crash = 0
    while q:
        x,y = q.popleft()
        if x==N and y==M:
            print(visited[x][y]-1)
            return True
        for i in range(4):
            nx,ny = x+d[i][0] + y+d[i][1]
            if


N,M = map(int,input().split())
lst = [list(map(int, input())) for _ in range(N)]
r,c=1,1
visited = [[0]*M for _ in range(N)]
visited[r][c]=1
bfs(r,c,N,M)