# pgms 77485 2021 dev-match 행렬 테두리 회전하기
# 에엥 타임에러............................... 머지?...........
# https://school.programmers.co.kr/questions/29760 내일 오면 이거 읽어보기

rows = 100
columns = 97
queries = 	[[1,1,100,97]]
# res = [1]

d = [(0,1), (1,0), (0,-1), (-1,0)]#우 하 좌 상

def solution(rows, columns, queries):
    map = [[0] * rows for _ in range(columns)]  # map 만들기 . ..
    cnt = 1
    for i in range(columns):
        for j in range(rows):
            map[i][j] = cnt
            cnt += 1
    print(map)
    answer = []
    for i in queries:
        x1,y1,x2,y2 = i[0]-1, i[1]-1, i[2]-1, i[3]-1 #인덱스화해서 나누기. 고정놈들
        x,y = x1,y1 #움직일놈들
        tmp = map[x][y]
        tmpans = []
        didx= 0
        while True:
            nx, ny = x+d[didx][0], y+d[didx][1]
            if 0<=nx<columns and 0<=ny<rows:
                tmpans.append(tmp)
                tmp, map[nx][ny] = map[nx][ny], tmp #바꾸고
                x, y = nx, ny #인덱스도 옮겨주고
                if didx==0 and y==y2: didx+=1
                elif didx==1 and x==x2: didx+=1
                elif didx==2 and y==y1: didx+=1
                elif didx==3 and x==x1: break
        answer.append(min(tmpans))


    return answer

print(solution(rows, columns, queries))