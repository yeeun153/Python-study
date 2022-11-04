#응용실습(신지우)
v1=int(input("첫번째 정수를 입력하세요:")) #사용자 입력
v2=int(input("두번째 정수를 입력하세요:"))

def triangle(v1,v2):  #triangle 함수 정의
    result=0
    result=v1*v2*1/2  #삼각형 넓이 값을 구함
    return result

def quadrangle(v1,v2):  #quadrangle 함수 정의
    result=0
    result=v1*v2      #사각형 넓이 값을 구함
    return result


trianglecal=triangle(v1,v2)
quadranglecal=quadrangle(v1,v2)

print("삼각형 넓이는 %.2f, 사각형의 넓이는 %s입니다."%(trianglecal,quadranglecal))  #출력

#응용실습(손예은)
def cal(v1,v2,op):  #(첫번째 수, 두번째 수, 부호) cal 함수 정의
    result=0
    if op=='+':    #'+'일 때
        result=v1+v2 #계산
    elif op=='-':    #'-'일 때
        result=v1-v2  #계산
    elif op=='*':    #'*'일 때
        result=v1*v2  #계산
    else:            #'/'일 때
        result=v1/v2  #계산
    return result


c=input("계산을 입력하세요(+,-,*,/):") #사용자 입력
a=int(input("첫 번째 수를 입력하세요:"))
b=int(input("두 번째 수를 입력하세요:"))
res=cal(a,b,c)
print("##계산기:%d %s %d=%d"%(a,c,b,res)) #출력

#응용실습(김다은)
def cal(v1,v2,op): #cal 함수 정의
    result=0
    if op=='+':  #'+'일 때
        result=v1+v2 #계산
    elif op=='-':  #'-'일 때
        result=v1-v2  #계산
    elif op=='*':  #'*'일 때
        result=v1*v2  #계산
    elif op=='/':  #'/'일 때
        result=v1/v2  #계산
    else:         #'**'일 때
        result=v1**v2  #계산
    return result

a=int(input("첫 번째 수를 입력하세요:"))  #사용자 입력
c=input("계산을 입력하세요(+,-,*,/,**):")
b=int(input("두 번째 수를 입력하세요:"))

if c=='/': #'/'일 때
    if b==0: #'b==0'이면
        print("0으로는 나누면 안 됩니다.ㅠㅠ") #출력
    elif b!=0:
        res=cal(a,b,c)
        print("##계산기:%d %s %d=%d"%(a,c,b,res)) 
else:
    res=cal(a,b,c)
    print("##계산기:%d %s %d=%d"%(a,c,b,res)) #출력
