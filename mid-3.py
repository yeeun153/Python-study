#Q3
grade={}
l_a=[]
l_b=[]

while True:
    a=input('과목명:')
   
    if not a:
        break
    b=int(input('점수:'))
    grade[a]=b
    l_a.append(a)
    l_b.append(b)

hap=0
for a,b in zip(l_a,l_b):
    print(a,b)

hap=sum(l_b)
print('합계는 %d점 입니다.'%hap)
avg=sum(l_b)/len(l_a)
print('평균은 %.1f점 입니다.'%avg)
    
    

    

