v1=int(input("첫번째 정수를 입력하세요:"))
v2=int(input("두번째 정수를 입력하세요:"))

def triangle(v1,v2):
    result=0
    result=v1*v2*1/2
    return result

def quadrangle(v1,v2):
    result=0
    result=v1*v2
    return result


trianglecal=triangle(v1,v2)
quadranglecal=quadrangle(v1,v2)

print("삼각형 넓이는 %.2f, 사각형의 넓이는 %s입니다."%(trianglecal,quadranglecal))
