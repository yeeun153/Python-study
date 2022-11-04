#Q1
import random
menu=[("1. 이상형 추가"),("2. 결정하기"),("3. 이상형 명단보기"),("4. 새로 입력하기"),("5. 종료")]
ideal=[]

print('===')
print('1. 이상형 추가')
print('2. 결정하기')
print('3. 이상형 명단보기')
print('4. 새로 입력하기')
print('5. 종료')
num=int(input())

while True:

    if num==1:
        a=input('당신의 이상형은?')
        ideal.append(a)

    elif num==2:
        print('당신의 이상형은',random.choice(ideal))

    elif num==3:
        print(ideal)

    elif num==4:
        ideal.clear()

    elif num==5:
        break

    print('1. 이상형 추가')
    print('2. 결정하기')
    print('3. 이상형 명단보기')
    print('4. 새로 입력하기')
    print('5. 종료')
    num=int(input())
