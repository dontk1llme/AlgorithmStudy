# boj 2138 전구와 스위치
# https://dogsavestheworld.tistory.com/137
# https://velog.io/@dding_ji/baekjoon2138
# 첫 스위치를 누르는 경우와 누르지 않는 경우로 분리!! <--- 이 생각 못 해서 헤맴...
# 마지막 스위치도 i+1 없는 거 주의


def change(now, to):
    l = now[:]
    press = 0
    for i in range(1, N): #0번째는 밑에서 보니까
        #이전 전구가 같은 상태면 pass (1,2,3 중 무조건 1을 기준으로 해야함.)
        if l[i-1] == to[i-1]:
            continue
        #다르면
        press+=1
        for j in range(i-1, i+2):
            if j<N: #범위 내
                l[j]=1-l[j] #1이면 0되고 0이면 1됨
    return press if l==to else 1e9 #0번째 한 경우 안 한 경우 비교해야 해서 바로 -1 안때리고 1e9

N = int(input())
now = list(map(int,input()))
to = list(map(int,input()))

#첫 전구의 스위치를 누르지 않는 경우
ans = change(now, to)
#누르는 경우
now[0]=1-now[0]
now[1]=1-now[1]
ans = min(ans, change(now, to)+1)
print(ans if ans!=1e9 else -1)
