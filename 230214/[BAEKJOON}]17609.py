# [BOJ] 17609 - 회문
# 회문:0, 유사회문: 1, 그 외: 2
#
# 슬라이싱 한 번이 O(N)이라서 시간초과................................
# -> 앞뒤 하나하나 비교하는 방식으로 가야함.

# try1 - 시간초과
# def check(string):
#     if string[::-1] == string: #회문
#         return 0
#     else: #유사회문 or 그 외
#         for i in range(len(string)):
#             newstr = string[:i]+string[i+1:]
#             if newstr[::-1]==newstr: #유사회문
#                 return 1
#             else: continue
#         return 2
#
#
# T = int(input())
# for tc in range(1, T+1):
#     s = input()
#     print(check(s))
# /////////////////////////////////////////////////////////////////////

# try2  틀렸다는데? 예제는 맞는데 1%에서 멈춤. 아마도 버퍼문제
# T = int(input())
# for tc in range(1, T + 1):
#     s = input()
#     ans = 0
#     while len(s) > 1:
#         if s[0] == s[-1]: #앞뒤 같을 때
#             s = s[1:-1]
#         elif s[0]==s[-2]:
#             s = s[1:-1]
#             ans=1
#         elif s[1]==s[-1]:
#             s = s[2:-1]
#             ans=1
#         else:
#             ans=2
#             break
#     print(ans)
#////////////////////////////////////////////////////////////////////
# try3 결국 구글링.
# 투포인터 사용. 파이썬에서 투포인터는 써 본 적 없어서 연습 필요
# abca 하면 1 나와야 하는데 2 나옴.
# def check(string):
#     left=0
#     right=len(string)-1 #인덱스로 해야하니까
#
#     while left<right:
#         if string[left] == string[right]:
#             left+=1
#             right-=1
#         else:
#             if left<right-1:
#                 temp = string[:right]+string[right+1:]
#                 if temp[:] == temp[::-1]:
#                     return 1
#             if left+1<right:
#                 temp = string[:left]+string[left+1:]
#                 if temp[:] == temp[::-1]:
#                     return 1
#             return 2
#     return 0
#
# T = int(input())
# for i in range(T):
#     s=input()
#     print(check(s))
#////////////////////////////////////////////////////////
#try4 - 아 몰라
# https://velog.io/@rlawogks2468/%EB%B0%B1%EC%A4%80-17609-%ED%9A%8C%EB%AC%B8-Greedy-with-Python
# 왼쪽에서 한칸 건너 뛴 다음 비교
# 오른쪽에서 한칸 건너 뛴 다음 비교
# !! 이거 !!
# 여기서 중요한점은 1, 2번을 비교한뒤에 또 일치하지 않는 문자가 나온다면 회문이 아니기 때문에 따로 함수를 만들어서 또 일치하지 않는 문자가 나오는지 확인해줘야 한다.

def finalCheck(str, left, right):
    while left < right:
        if str[left] == str[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


def checkIsSame(str, left, right):
    if str == str[::-1]:  # 바로 회문인 경우
        return 0
    while left < right:  # 1 or 2
        if str[left] == str[right]:  # 같으면 한칸씩 이동
            left += 1
            right -= 1
        else:
            leftCheck = finalCheck(str, left + 1, right)  # 왼쪽 한칸 건너뜀
            rightCheck = finalCheck(str, left, right - 1)  # 오른쪽 한칸 건너뜀
            if leftCheck or rightCheck:  # 다른 문자 안나왔으면 회문임
                return 1
            else:  # 다른 문자 나온 경우
                return 2
    return 1


t = int(input())

for i in range(t):
    str = input()
    print(checkIsSame(str, 0, len(str) - 1))

