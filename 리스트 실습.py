#1
print('**** 10개의 단어를 입력받아 역순으로 출력 ****')
i=0
numbers=[]
numbers=[None]*10
for i in range(10):
   numbers[i]=int(input("단어입력(%d):"%(i+1)))

numbers.reverse()
for i in numbers:
   print(i)


#2
print('**** 10개의 정수를 입력받아 역순으로 양수만 출력 ****')
i=0
numbers=[]
numbers=[None]*10
for i in range(10):
   numbers[i]=int(input("%d.정수입력:"%(i+1)))

for number in numbers[::-1]:
    if number>0:
        print(number)


#3
print('**** n개의 정수를 입력받아 역순으로 양수만 출력 ****')
i=0
num=int(input("몇 개의 정수를 입력합니까?:"))
numbers=[None]*num #리스트 갯수, 크기 결정
for i in range(num): # 갯수만큼 반복
   numbers[i]=int(input("(%d/%d)정수입력:"%(i+1,num))) # 입력을 받아서 숫자로 변환해서 저장

for number in numbers[::-1]: # 역순으로 읽어드림
    if number>0: # 내용이 양수인지여부
        print(number) # 출력


#4
print('**** n개의 정수를 입력받아 인덱스가 홀수 위치의 요소 중 짝수만 출력 ****')
i=0
num=int(input("몇 개의 정수를 입력합니까?:"))
numbers=[None]*num
for i in range(num):
    numbers[i]=int(input("(%d/%d)정수입력:"%(i+1,num)))

for i in range(num):
    if i%2!=0 and numbers[i]%2==0:
        print(numbers[i])


#5
print('**** n개의 정수를 입력받아 합과 평균을 출력하기 ****')
i=0
num=int(input("몇 개의 과목의 점수를 입력합니까?:"))
numbers=[None]*num
for i in range(num):
   numbers[i]=int(input("%d.과목 점수:"%(i+1)))

total=0
for i in range(num):
   total=total+numbers[i]
average=total/num
print("합:%d, 평균:%d"%(total,average))


#6
i=0
a,b,ab,o=0,0,0,0

for i in range(10):
    print("\n헌혈해 주셔서 감사합니다.헌혈하신 혈액형을 선택하세요.")
    blood=input("A,B,AB,O:")
    if blood=="A":
        a+=1
    elif blood=="B":
        b+=1
    elif blood=="AB":
        ab+=1
    elif blood=="O":
        o+=1
     
print("--------------------------------")
print("혈액형:개수")
print("--------------------------------")

print("A형:%d"%a)
print("B형:%d"%b)
print("AB형:%d"%ab)
print("O형:%d"%o)
input("===== Enter를 누르세요 =====")


#7
questions=(["3+2",5,3],["5/2의 몫",2,5],["10-2",8,3],["10의2제곱*2",200,5],["1-(10나누기4의 나머지)",-1,5],["2의4제곱",16,3],["4/2",2,3])
correct=0
not_correct=0
score=0

for question in questions:
    print('문제',':',end=question[0])
    answer=int(input("\n정답을 입력하세요."))

    if question[1]==answer:
        correct+=1
        score+=question[2]
    elif question[1]!=answer:
        not_correct+=1
    
print("------------------------------")
print("정답 개수:%d" %correct)
print("오답 개수:%d" %not_correct)
print("Total Score          :%d" %score)
print("------------------------------")
input("===== Enter를 누르세요 =====")


#8
login={}

while True:
    num=int(input('\n1.회원가입, 2.프로그램 종료    '))

    if num==1:
        key=input("아이디를 입력하세요.")
        values=input("비밀번호를 입력하세요.")
        login[key]=values

        
    elif num==2:
        print('------------------------------')
        print('아이디 : 비밀번호')
        print('------------------------------')
        print(login)
        print('------------------------------')


#8
login={}
l_key=[]
l_values=[]

while True:
    num=int(input('\n1.회원가입, 2.프로그램 종료    '))

    if num==1:
        key=input("아이디를 입력하세요.")
        values=input("비밀번호를 입력하세요.")
        login[key]=values
        l_key.append(key)
        l_values.append(values)

    elif num==2:
        print('------------------------------')
        print('아이디 : 비밀번호')
        print('------------------------------')
        
        for k,v in zip(l_key,l_values):
            print(k,':',v)
