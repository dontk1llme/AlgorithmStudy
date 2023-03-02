# BOJ 1091 카드섞기
# https://nkw011.github.io/baekjoon/baekjoon-1091/


n = int(input())
P = input().split()
S = list(map(int,input().split()))

visited = set()
answer,cnt = '012' * (n//3), 0
while True:
    seq = "".join(P)
    if seq == answer:
        break
    if seq in visited:
        cnt = -1
        break
    visited.add(seq)
    temp = [0] * n
    for i in range(n):
        temp[S[i]] = P[i]
    P = temp
    cnt += 1
print(cnt)
