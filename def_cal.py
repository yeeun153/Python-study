def cal(v1,v2,op):
    result=0
    if op=='+':
        result=v1+v2
    elif op=='-':
        result=v1-v2
    elif op=='*':
        result=v1*v2
    else:
        result=v1/v2
    return result


c=input("계산을 입력하세요(+,-,*,/):")
a=int(input("첫 번째 수를 입력하세요:"))
b=int(input("두 번째 수를 입력하세요:"))
res=cal(a,b,c)
print("##계산기:%d %s %d=%d"%(a,c,b,res))
