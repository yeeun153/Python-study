#Q1(김다은)

import random #random 패키지를 사용해 무작위 선택
menu=[("1. 간식 추가"),("2. 결정하기"),("3. 간식 목록보기"),("4. 새로 입력하기"),("5. 종료")]
dessert=[] #리스트 생성
i=0

name=input("사용자의 이름을 입력해주세요:")
print('===')
print('1. 간식 추가')
print('2. 결정하기')
print('3. 간식 목록보기')
print('4. 새로 입력하기')
print('5. 종료')
num=int(input())

while True:

    if num==1:
        a=input('원하는 간식은?')
        dessert.append(a) #리스트에 항목 추가
        i+=1

    elif num==2:
        R_dessert=random.choice(dessert) #랜덤 선택
        print('오늘의 간식은 %s'%R_dessert)
        print('%d개의 간식 중에 %s 선택'%(i,R_dessert))
        print('%s님께 추천 간식은 %d개 중 %s입니다.'%(name,i,R_dessert))

    elif num==3:
        print(dessert) #출력

    elif num==4:
        dessert.clear() #항목 제거

    elif num==5:
        break

    print('1. 이상형 추가')
    print('2. 결정하기')
    print('3. 간식 목록보기')
    print('4. 새로 입력하기')
    print('5. 종료')
    num=int(input())
