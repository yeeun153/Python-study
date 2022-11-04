#카페 주문 프로그램
ame=0
lat=0
mac=0
while True:
    print("\n===== 슈먼 카페 =====")
    print('1. 아메리카노: 2000원')
    print('2. 카페라떼: 2500원')
    print('3. 마끼야또: 3000원')
    print('4. 주문종료\n')
    a=int(input('메뉴를 입력해주세요=>'))


    while a<=3:
        if a==1:
            b=int(input('수량을 입력해주세요=>'))
            ame=ame+b
            
        elif a==2:
            b=int(input('수량을 입력해주세요=>'))
            lat=lat+b

        elif a==3:
            b=int(input('수량을 입력해주세요=>'))
            mac=mac+b

       


        print('\n**** 총 주문내역 ****')
        print('1. 아메리카노:',ame,'잔')
        print('2. 카페라떼:',lat,'잔')
        print('3. 마끼야또:',mac,'잔')
        print('총금액:%d원'%(ame*2000+lat*2500+mac*3000))

        print("\n===== 슈먼 카페 =====")
        print('1. 아메리카노: 2000원')
        print('2. 카페라떼: 2500원')
        print('3. 마끼야또: 3000원')
        print('4. 주문종료\n')
        a=int(input('메뉴를 입력해주세요=>'))

    if a>=5:
        print('잘못 입력되었습니다. 다시 입력해주세요.')
        print('\n**** 총 주문내역 ****')
        print('1. 아메리카노:',ame,'잔')
        print('2. 카페라떼:',lat,'잔')
        print('3. 마끼야또:',mac,'잔')
        print('총금액:%d원'%(ame*2000+lat*2500+mac*3000))
        continue
        
       


    elif a==4:
        print('주문을 종료합니다.')
        print('\n**** 총 주문내역 ****')
        print('1. 아메리카노:',ame,'잔')
        print('2. 카페라떼:',lat,'잔')
        print('3. 마끼야또:',mac,'잔')
        print('총금액:%d원'%(ame*2000+lat*2500+mac*3000))
    break


