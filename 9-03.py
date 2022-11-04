#Q3(손예은)
number=int(input("몇 명을 입력하나요?")) #학생 수 입력
name=[] #리스트 생성
sub=[]
score=[]
total=[]
avg=[]
for i in range(0,number,1): #반복 범위 
    name.append(input("%d번 학생 이름:"%(i+1)))
    total.append(0)
    for a in range(0,3,1): #반복 개수
         sub.append(input("과목:"))
         while True:
             s=input("점수:")
             if s.isnumeric()==True: #숫자인지 확인하는 함수
                 score.append(int(s))
                 total[i]+=int(s) #점수 합계
                 break


    avg.append(total[i]/3)
    print("%s 총점은 %d점 입니다."%(name[i],total[i])) #출력
    print("%s 평균은 %.1f점 입니다."%(name[i],avg[i])) #평균 소수 한 자리까지 출력
    sub.clear()
    score.clear()
for i in range(i,number,1): #평균 1등 학생 찾기
    max=0
    if (avg[max]<avg[i]):
        max=i
    else:
        max=max
print("평균 1등인 학생은 %s입니다."%name[max]) #출력
