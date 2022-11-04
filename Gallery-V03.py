#Gallery-V03(손예은)
#강의자료의 사진을 첨부하여 이미지 압축파일은 제출하지 않았습니다.
from tkinter import*
window = Tk()
window.title("사진 앨범 보기")
window.geometry("700x500")

a = 1

photo1 = PhotoImage(file = "gif/cat5.gif")
photo2 = PhotoImage(file = "gif/cat4.gif")
photo3 = PhotoImage(file = "gif/cat2.gif")
photo4 = PhotoImage(file = "gif/cat3.gif")

def myFunc():
    global a
    if a>4:
        a = 1
    elif a<0:
        a = 4
    if a == 1:
        label1.configure(image = photo1)
    elif a == 2:
        label1.configure(image = photo2)
    elif a == 3:
        label1.configure(image = photo3)
    else:
        label1.configure(image = photo4)
        
button1 = Button(window, text = "<<이전", command = myFunc)
button2 = Button(window, text = "다음>>", command = myFunc)
        
if a>4:
    a = 1
elif a<0:
    a = 4

def clickLEFT(event):
    global a
    if a>4:
        a = 1
    elif a<0:
        a = 4
    else:
        a -= 1
def clickRIGHT(event):
    global a
    if a>4:
        a = 1
    elif a<0:
        a = 4
    else:
        a += 1

if a == 1:
    label1 = Label(window, image = photo1)
elif a == 2:
    label1 = Label(window, image = photo2)
elif a == 3:
    label1 = Label(window, image = photo3)
else:
    label1 = Label(window, image = photo4)

button1.bind("<Button>",clickLEFT)
button2.bind("<Button>",clickRIGHT)

button1.place(x=250,y=10)
button2.place(x=400,y=10)
label1.place(x=230,y=200)
window.mainloop()
