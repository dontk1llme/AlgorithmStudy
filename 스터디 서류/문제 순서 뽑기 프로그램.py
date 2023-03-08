import random

member = ['이예슬', '진익근', '이성우', '송준우', '최홍준', '최태호', '정현아','서동훈','김하늘']
random.shuffle(member)

#오늘 몇 명이죠?
N = 5 #명+1

print('~*~이번 주 담당 문제 랜덤 돌리기~*~')
for i in range(1,N):
   print(f'{i}번: {member[i-1]}')

print('~~~~~~~다들 파이팅~~~~~~~')