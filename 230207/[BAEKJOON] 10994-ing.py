# [BAEKJOON] 10994 별 찍기 - 19
# https://ansohxxn.github.io/boj/10994/
# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=kckyoung2&logNo=221040753895


# line이 홀수일 때와 짝수일 때의 규칙이 다름.
# 홀수: 인덱스 1, -2 -> 1,3,-4,-2 이렇게 바꾸면서 출력.
#       근데 줄도 마찬가지.로... 0,-1 / 2,-3 이렇게 

N = int(input())

def star(N):
    line = 1+4*(N-1)
    star = [['*']*(line) for _ in range(line)]
    # 홀수줄(첫줄부터, 인덱스기준 아님)
    for i in range(0,len(star),2):
        blank=1
        for j in range(len(star)):

            

    
    # 짝수줄(둘째줄부터)
    for i in range(1,len(star)-1,2):
        pass








    #출력
    for i in range(line):
        for j in range(line):
            print(star[i][j], end='')
        print()
    # while N>0:
    #     if N%2==1:
    #         print('*')*N
    #     else: 
    #         print('*', ' '*N, '*')
    #         print()

star(N)