#1
def plus(v1,v2):
    result=0
    result=v1+v2
    return result

hap=0

hap=plus(100,200)
print("100과 200의 plus() 함수 결과는 %d" %hap)

#2
coffee=0

coffee=int(input("어떤 커피 드릴까요?(1:보통,2:설탕,3:블랙)"))

print()
print("#1. 뜨거운 물을 준비한다.");
print("#2. 종이컵을 준비한다.");

if coffee==1:
    print("#3. 보통커피를 탄다.")
elif coffee==2:
    print("#3. 설탕커피를 탄다.")
elif coffee==3:
    print("#3. 블랙커피를 탄다.")
else:
    print("#3. 아무거나 탄다.\n")

print("#4. 물을 붓는다.");
print("#5. 스푼으로 젓는다.");
print()
print("손님~커피 여기 있습니다.");

#3
coffee=0

def coffee_machine(button):
    print()
    print("#1.(자동으로) 뜨거운 물을 준비한다.");
    print("#2.(자동으로) 종이컵을 준비한다.");

    if button==1:
        print("#3.(자동으로)보통커피를 탄다.")
    elif button==2:
        print("#3.(자동으로)설탕커피를 탄다.")
    elif button==3:
        print("#3.(자동으로)블랙커피를 탄다.")
    else:
        print("#3.(자동으로)아무거나 탄다.\n")

    print("#4.(자동으로) 물을 붓는다.");
    print("#5.(자동으로) 스푼으로 젓는다.");
    print()

coffee=int(input("어떤 커피 드릴까요?(1:보통,2:설탕,3:블랙)"))
coffee_machine(coffee)
print("손님~커피 여기 있습니다.");

#4
coffee=0

def coffee_machine(button):
    print()
    print("#1.(자동으로) 뜨거운 물을 준비한다.");
    print("#2.(자동으로) 종이컵을 준비한다.");

    if button==1:
        print("#3.(자동으로)보통커피를 탄다.")
    elif button==2:
        print("#3.(자동으로)설탕커피를 탄다.")
    elif button==3:
        print("#3.(자동으로)블랙커피를 탄다.")
    else:
        print("#3.(자동으로)아무거나 탄다.\n")

    print("#4.(자동으로) 물을 붓는다.");
    print("#5.(자동으로) 스푼으로 젓는다.");
    print()

coffee=int(input("A손님, 어떤 커피 드릴까요?(1:보통,2:설탕,3:블랙)"))
coffee_machine(coffee)
print("A손님~커피 여기 있습니다.")

coffee=int(input("B손님, 어떤 커피 드릴까요?(1:보통,2:설탕,3:블랙)"))
coffee_machine(coffee)
print("B손님~커피 여기 있습니다.")

coffee=int(input("C손님, 어떤 커피 드릴까요?(1:보통,2:설탕,3:블랙)"))
coffee_machine(coffee)
print("C손님~커피 여기 있습니다.")

#5
def func1():
    a=10
    print("func1()에서 a값 %d"%a)

def func2():
    print("func2()에서 a값 %d"%a)

a=20

func1()
func2()
