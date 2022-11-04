#Code10-01
from tkinter import*

window=Tk()

window.mainloop()

#Code10-02
from tkinter import*

window=Tk()
window.title("윈도창 연습")
window.geometry("400x100")
window.resizable(width=FALSE,height=FALSE)

window.mainloop()

#Code10-03
from tkinter import*
window=Tk()

label1=Label(window,text="COOKBOOK~~Python을")
label2=Label(window,text="열심히",font=("궁서체",30),fg="blue")
label3=Label(window,text="공부 중입니다.",bg="magenta",width=20,height=5,anchor=SE)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()

#Code10-04
from tkinter import*
window=Tk()

photo=PhotoImage(file="gif/dog.gif")
label1=Label(window,image=photo)

label1.pack()

window.mainloop()

#Code10-05
from tkinter import*
window=Tk()

photo1=PhotoImage(file="gif/cat.gif")
photo2=PhotoImage(file="gif/cat2.gif")

label1=Label(window,image=photo1)
label2=Label(window,image=photo2)

label1.pack(side=LEFT);
label2.pack(side=LEFT);

window.mainloop()

#Code10-06
from tkinter import*
from tkinter import messagebox

def myFunc():
    messagebox.showinfo("강아지 버튼","강아지가 귀엽죠?^^")

window=Tk()

photo=PhotoImage(file="gif/dog2.gif")
button1=Button(window,image=photo,command=myFunc)

button1.pack()

window.mainloop()

#Code10-07
from tkinter import*
from tkinter import messagebox
window=Tk()

def myFunc():
    if chk.get()==0:
        messagebox.showinfo("","체크버튼이 꺼졌어요.")
    else:
        messagebox.showinfo("","체크버튼이 켜졌어요.")

chk=IntVar()
cb1=Checkbutton(window,text="클릭하세요",variable=chk,command=myFunc)

cb1.pack()
window.mainloop()

#Code10-08
from tkinter import*
window=Tk()

def myFunc():
    if var.get()==1:
        label1.configure(text="파이썬")
    elif var.get()==2:
        label1.configure(text="C++")
    else:
        label1.configure(text="Java")


var=IntVar()
rb1=Radiobutton(window,text="파이썬",variable=var,value=1,command=myFunc)
rb2=Radiobutton(window,text="C++",variable=var,value=2,command=myFunc)
rb3=Radiobutton(window,text="Java",variable=var,value=3,command=myFunc)

label1=Label(window,text="선택한 언어:",fg="red")

rb1.pack()
rb2.pack()
rb3.pack()
label1.pack()

window.mainloop()

#Code10-09
from tkinter import*
window=Tk()

button1=Button(window,text="버튼1")
button2=Button(window,text="버튼2")
button3=Button(window,text="버튼3")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)

window.mainloop()

#Code10-10
from tkinter import*
window=Tk()

btnList=[None]*3

for i in range(0,3):
    btnList[i]=Button(window,text="버튼"+str(i+1))

for btn in btnList:
    btn.pack(side=RIGHT)

window.mainloop()

#Code10-11
from tkinter import*


btnList=[None]*9
fnameList=["froyo.gif","gingerbread.gif","honeycomb.gif","icecream.gif","jellybean.gif","kitkat.gif","lollipop.gif","marshmallow.gif","nougat.gif"]
photoList=[None]*9
i,k=0,0
xPos,yPos=0,0
num=0


window=Tk()
window.geometry("210x201")

for i in range(0,9):
    photoList[i]=PhotoImage(file="gif/"+fnameList[i])
    btnList[i]=Button(window,image=photoList[i])

for i in range(0,3):
    for k in range(0,3):
        btnList[num].place(x=xPos,y=yPos)
        num+=1
        xPos+=70
    xPos=0
    yPos+=70

window.mainloop()

#Code10-13
from tkinter import*
from tkinter import messagebox

def clickLeft(event):
    messagebox.showinfo("마우스","마우스 왼쪽 버튼이 클릭됨")

window=Tk()

window.bind("<Button-1>",clickLeft)

window.mainloop()

#Code10-14
from tkinter import*
from tkinter import messagebox


def clickImage(event):
    messagebox.showinfo("마우스","토끼에서 마우스가 클릭됨")


window=Tk()
window.geometry("400x400")

photo=PhotoImage(file="gif/rabbit.gif")
label1=Label(window,image=photo)

label1.bind("<Button>",clickImage)

label1.pack(expand=1,anchor=CENTER)
window.mainloop()

#Code10-15
from tkinter import*

def clickMouse(event):
    txt=""
    if event.num==1:
        txt+="마우스 왼쪽 버튼이("
    elif event.num==3:
        txt+="마우스 오른쪽 버튼이("

    txt+=str(event.y)+","+str(event.x)+")에서 클릭됨"
    label1.configure(text=txt)

window=Tk()
window.geometry("400x400")

label1=Label(window,text="이곳이 바뀜")

window.bind("<Button>",clickMouse)

label1.pack(expand=1,anchor=CENTER)
window.mainloop()

#Code10-16
from tkinter import*
from tkinter import messagebox


def keyEvent(event):
    messagebox.showinfo("키보드 이벤트","눌린 키:"+chr(event.keycode))


window=Tk()

window.bind("<Key>",keyEvent)

window.mainloop()
