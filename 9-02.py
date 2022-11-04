#Q2(신지우)
name_book={} #딕셔너리 생성
stu1=0
stu2=0
stu3=0
a=[]
b=[]
c=[]


while True:
    name=input("(입력모드)이름을 입력하시오:")
    

    if len(name)==0:
        while name!=(len(name)==0):
            name=input("(검색모드)이름을 입력하시오:")

        
            if name in name_book:                  
                print("%s 학생의 학과는 %s입니다."%(name,name_book[name]))
                subname=input("학과를 입력하시오:")
                
                if subname=="정보보호":
                    stu1+=1
                    print("학생수:%d"%stu1)
                    print("학생이름:%s"%a)  #학과가 정보보호학과이면  학생 수 +1,학생이름 출력
                elif subname=="소프트웨어융합":
                    stu2+=1
                    print("학생수:%d"%stu2)
                    print("학생이름:%s"%b)  #학과가 소프트웨어융합학과면 학생 수 +1,학생이름 출력
                elif subname=="디지털미디어":
                    stu3+=1
                    print("학생수:%d"%stu3)
                    print("학생이름:%s"%c)  #학과가 디지털미디어학과면 학생 수 +1,학생이름 출력
                    
            elif len(name)==0:
                break
            else:
                print("%s 학생은 없습니다."%name)

    elif name in name_book:
        input("학과를 입력하시오:")
        input("(입력모드)이름을 입력하시오:")
        fix=input("(수정모드)학과를 입력하시오:")
        name_book[name]=fix #수정된 학과 저장
        if sub=="정보보호":
            stu1+=1
            a.append(name) #리스트에 이름 추가
        elif sub=="소프트웨어융합":
            stu2+=1
            b.append(name)
        else:
            stu3+=1
            c.append(name)


    elif name=="Q":
        break

    else:
        sub=input("학과를 입력하시오:") #학과 입력 받음
        name_book[name]=sub #입력받은 학과 저장
        if sub=="정보보호":
            a.append(name)
        elif sub=="소프트웨어융합":
            b.append(name)
        else:
            c.append(name)
