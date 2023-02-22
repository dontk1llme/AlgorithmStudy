# 14888 연산자 끼워넣기
# 왜 제대로 안나옴? ????????????

N = int(input())
num = list(map(int, input().split())) #숫자
op = list(map(int, input().split())) #연산자
min_ = int(1e9)
max_ = -int(1e9)
ans = num[0]

def dfs(idx):
    global ans
    global min_, max_

    if idx==N: #인덱스값이 N과 같으면 최대, 최소 찾기
        if ans > max_: max_ = ans
        if ans < min_: min_ = ans
        return

    for i in range(4): #연산
        tmp = ans
        if op[i]>0:
            if i==0: ans+= num[idx]
            elif i==1: ans-=num[idx]
            elif i==2: ans*=num[idx]
            else:
                if ans>=0: ans//=num[idx]
                else: ans = (-ans//num[idx])*-1
        op[i]-=1
        dfs(idx+1)
        ans = tmp
        op[i]+=1 #왜 더하는지를 모르겟네

dfs(1)
print(max_)
print(min_)
