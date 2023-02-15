# [BOJ] 9251 LCS
# 첨에는 부분집합 생각함. 근데 그게 그거임.
# DP 사용해야 함. 하나하나->큰거 봐야하니까.
# 엑셀처럼?? 겹치는 부분 세면 되는 거 아님?
# -> 2차원배열 만들어서
# https://bgspro.tistory.com/134 표 참고해서 이해하세요

s1 = input() # 기준
s2 = input() # 하나씩 증가시키며 비교할것
lst = [list([0]*len(s2+1)) for _ in range(len(s1+1))] #인덱스 편하게 하려고 하나씩 늘려줌 (블로그에서 착안)
print(lst)

for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i] == s2[j]:
            lst[i][j]+=lst[i-1][j-1]+1
        else:


