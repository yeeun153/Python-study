##Gallert-V02(신지우)##
from tkinter import*
window = Tk()
window.title("사진 앨범 보기")
window.geometry("700x500")

a = 1

photo1 = PhotoImage(file = "gif/jeju1.gif")
photo2 = PhotoImage(file = "gif/jeju2.gif")
photo3 = PhotoImage(file = "gif/jeju3.gif")
photo4 = PhotoImage(file = "gif/jeju4.gif")



def myFunc():
    global a
    if a>4:
        a = 1
    elif a<0:
        a = 4
    if a == 1:
        label1.configure(image = photo1)
        label2.configure(text = "jeju1.gif")
    elif a == 2:
        label1.configure(image = photo2)
        label2.configure(text = "jeju2.gif")
    elif a == 3:
        label1.configure(image = photo3)
        label2.configure(text = "jeju3.gif")
    else:
        label1.configure(image = photo4)
        label2.configure(text = "jeju4.gif")
        

#버튼 생성#
button1 = Button(window, text = "<<이전", command = myFunc)
button2 = Button(window, text = "다음>>", command = myFunc)
        
#버튼 클릭#
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
    label2 = Label(window, text = "jeju1.gif")
elif a == 2:
    label1 = Label(window, image = photo2)
    label2 = Label(window, text = "jeju2.gif")    
elif a == 3:
    label1 = Label(window, image = photo3)
    label2 = Label(window, text = "jeju3.gif")
else:
    label1 = Label(window, image = photo4)
    label2 = Label(window, text = "jeju4.gif")

button1.bind("<Button>",clickLEFT)
button2.bind("<Button>",clickRIGHT)

button1.place(x=250,y=10)
label2.place(x=325,y=10)
button2.place(x=400,y=10)
label1.place(x=15,y=50)
window.mainloop()

