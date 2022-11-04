#Q2
phone_book={}

while True:
    a=input('(입력모드)이름을 입력하시오:')
    
    if not a:
        while True:
            c=input('(검색모드)이름을 입력하시오:')

            if c in phone_book:
                print(c,"의 전화번호는",phone_book[c],"입니다.")

            if not c:
                break


            elif not c in phone_book:
                print(c,"은 없습니다.")
            
    elif a in ["Q"]:
        break

    elif a in phone_book:
        input('전화번호를 입력하시오:')
        input('(입력모드)이름을 입력하시오:')
        d=input('(수정모드)전화번호를 입력하시오:')
        input('(입력모드)이름을 입력하시오:')
        e=input('(검색모드)이름을 입력하시오:')
        phone_book[e]=d
        print(e,"의 전화번호는",phone_book[e],"입니다.")
        input('전화번호를 입력하시오:')
        input('(검색모드)이름을 입력하시오:')

    else:
        b=input('전화번호를 입력하시오:')
        phone_book[a]=b
        
    
