#문제1(손예은)
a=int(input())
b=int(input())
print((a+b))

#문제 2(신지우)
a=input("문자열 입력:")
b=input("문자열 입력:")

if len(a)>len(b):
    print(a)
else:
    print(b)

#문제 3(김다은)
print("별(*)로 밑변과 높이가 N인 직각삼각형을 거꾸로 출력하려고 합니다.")
print("N은 1 이상 100 이하입니다.")
N=int(input("N을 입력해주세요:"))

for i in range(0,N,1):
    for k in range(0,N,1):
        print("*"*N)
        N-=1

#문제 4(손예은)
a=input()
print('"%s"'%a)

#문제 5(신지우)
num=int(input("\n숫자를 입력하세요:"))
if num>0:
    print(num)
else:
    print(0-num)

#문제 6(김다은)
print("입력받은 두 숫자가 같으면 두 숫자의 합을, 다르면 차를 출력하려고 합니다.")
print("입력하신 두번째 숫자는 첫번째 숫자와 같거나 커야합니다.")
N_1=int(input("첫번째 숫자를 입력해주세요:"))
N_2=int(input("두번째 숫자를 입력해주세요:"))
if N_1==N_2:
    total=N_1+N_2
    print(total)
else:
    total=N_2-N_1
    print(total)

#문제 7(손예은)
a=int(input())
for i in range(1,a+1):
    print(i)

#문제 8(신지우)
n=int(input("\n길이를 입력하세요:"))
arr=[None]*n
for i in range(0,n):
    arr[i]=int(input("값을 입력하세요:"))
for f in range(0,n-1,1):
    print(arr[f]-arr[f+1])

#문제 9(신지우)
number=int(input("\n자연수를 입력하세요:"))
print(int(str(number)[::-1]))

#문제 10(김다은)
print("문자열 s에서 '1'의 개수를 구하려 합니다")
print("문자열 s의 길이는 1 이상 1,000 이하입니다.")
print("문자열 s는 '1;~'9'로 이루어진 문자열입니다.")

s=input("문자열을 입력하세요:")
print(s.count('1'))
