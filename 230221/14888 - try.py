# 14888 연산자 끼워넣기
# 암튼 탐색임DFS 쓰면 될듯? bfs도 될거같긴한데...
# 수의 순서는 고정, 연산자는 경우의 수대로 다 넣어 보고 최소와 최대 구하기
# (-> 찾아보니 bfs는 시간복잡도가 높음)
# DFS함수에 입력받는 수열의 개수만큼 재귀적으로 함수 수행
# permutaion이 있긴 하던데 쓸 줄 몰라서 그냥... 배운 대로 하려고 해 봄 탐색 잘 못해서
# 참고 및 공부
# https://data-flower.tistory.com/72
# https://hongcoding.tistory.com/119

N = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split()) #덧셈, 뺄셈, 곱셈, 나눗셈(정수)

max_ = -1e9 #-10억
min_ = 1e9 #10억

def dfs(i,arr):
    global add, sub, mul, div, max_, min_
    if i==N: #주어진 수열을 다 받았을 경우 최대값과 최소값 계산
        max_ = max(max_, arr)
        min_ = min(min_, arr)
    else:
        if add>0: #더하기
            add-=1
            dfs(i+1, arr+A[i])
            add+=1
        if sub>0: #빼기
            sub-=1
            dfs(i+1, arr-A[i])
            sub+=1
        if mul>0: #곱하기
            mul-=1
            dfs(i+1, arr*A[i])
            mul+=1
        if div > 0:  # 나누기 정수라서 int처리 해줘야함
            div -= 1
            dfs(i + 1, int(arr / A[i]))
            div += 1
dfs(1,A[0])
print(max_)
print(min_)

#/////////////////////////////////////////////////////////////////
n = int(input())
number = list(map(int, input().split()))
op = list(map(int, input().split()))
minR = int(1e9)
maxR = -int(1e9)

answer = number[0]

def dfs(idx):
    global answer
    global minR, maxR

    if idx == n:
        if answer > maxR:
            maxR = answer
        if answer < minR:
            minR = answer
        return

    for i in range(4):
        tmp = answer
        if op[i] > 0:
            if i == 0:
                answer += number[idx]
            elif i == 1:
                answer -= number[idx]
            elif i == 2:
                answer *= number[idx]
            else:
                if answer >= 0:
                    answer //= number[idx]
                else:
                    answer = (-answer // number[idx]) * -1

            op[i] -= 1
            dfs(idx+1)
            answer = tmp
            op[i] += 1


dfs(1)
print(maxR)
print(minR)