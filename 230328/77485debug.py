#수형쓰

rows, columns, queries = 100, 97, [[1, 1, 100, 97]]

# 방향
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 2차원 맵 생성.
map = [[columns * i + j for j in range(1, columns + 1)] for i in range(rows)]
for i in map:
    print(i)
CNT=0
answer = []
for i in queries:
    # 각 꼭지점을 인덱스로 치환.
    x1, y1, x2, y2 = i[0] - 1, i[1] - 1, i[2] - 1, i[3] - 1
    x, y = x1, y1
    print("\n", "-" * 50)
    print("query : ", x1, y1, x2, y2)

    tmp = map[x][y]
    tmpans = []
    didx = 0

    while True:
        nx, ny = x + d[didx][0], y + d[didx][1]
        if nx == 97 and ny == 96:
            print(nx, ny, didx, columns, rows)
            CNT +=1
            if CNT ==3:
                break
#        print(x, x1, y, y1)

        print(nx, ny, didx)
        if 0 <= nx < columns and \
                0 <= ny < rows:
            print(23145)
            # 지나는 점 저장
            tmpans.append(tmp)

            # 거꾸로 가는 구나.
            tmp, map[nx][ny] = map[nx][ny], tmp

            # 넘어간다.
            x, y = nx, ny

            if didx == 0 and y == y2:
                didx += 1
            elif didx == 1 and x == x2:
                didx += 1
            elif didx == 2 and y == y1:
                didx += 1
            elif didx == 3 and x == x1:
                break

        answer.append(min(tmpans))


