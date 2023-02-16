# BOJ 2628 - 종이 자르기
# 배열 만들어서. 한번 자르면 그거 기준 위쪽, 왼쪽만 다 +N 해주기... 그래야 안 겹칠 거 같애
# 그렇게 수들 count 해서 제일 많은 애 몇 개 있는지 출력하면 되는 거잔아?
#??? 답 다 나오는데 틀렸대........ 뭐임???

X,Y = map(int, input().split()) #전체 종이 사이즈
paper = [[0]*X for _ in range(Y)]
N = int(input())

#입력받고 종이 자르기
for _ in range(N):
    a,b=map(int, input().split()) #자르기 시작할 위치 (a==0: 가로, 1: 세로)
    if a==0: #가로
        for i in range(b):
            for j in range(X):
                paper[i][j] +=N
    else: #세로
        for i in range(b):
            for j in range(Y):
                paper[j][i] +=N

# 최대값 찾기
paperlist =[]
for i in range(Y):
    for j in range(X):
        paperlist.append(paper[i][j])
paperlist.sort()

max = 0
cnt=0
paper= 0
for i in range(len(paperlist)-1):
    if paperlist[i]==paperlist[i+1]:
        cnt+=1
    else:
        cnt+=1
        papermax = paperlist[i]
        if max<cnt: max = cnt
        cnt=0
# print(papermax)
print(max)



