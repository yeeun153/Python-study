#그림판(손예은)
from tkinter import*
from tkinter.colorchooser import*
from tkinter.simpledialog import*

def mouseClick(event):
    global x1,y1,x2,y2
    x1=event.x
    y1=event.y

def mouseDrop(event):
    global x1,y1,x2,y2,penWidth,penColor
    x2=event.x
    y2=event.y
    canvas.create_line(x1,y1,x2,y2,width=penWidth,fill=penColor)

def getColor():
    global penColor
    color=askcolor()
    penColor=color[1]

def getWidth():
    global penWidth
    penWidth=askinteger("선 두께","선 두께(1~10)를 입력하세요",minvalue=1,maxvalue=10)

window=None
canvas=None
x1,y1,x2,y2=None,None,None,None 
penColor='black' #기본 색
penWidth=5 #기본 굵기

if __name__=="__main__":
    window=Tk()
    window.title("그림판 비슷한 프로그램")
    canvas=Canvas(window,height=300,width=300)

canvas.bind("<Button-1>",mouseClick)
canvas.bind("<ButtonRelease-1>",mouseDrop)
canvas.pack()

mainMenu=Menu(window)
window.config(menu=mainMenu)

fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="설정",menu=fileMenu)
fileMenu.add_command(label="선 색상 선택",command=getColor)
fileMenu.add_separator()
fileMenu.add_command(label="선 두께 결정",command=getWidth)

window.mainloop()

#메모장(신지우)

from tkinter import*
from tkinter.filedialog import*
import os

def saveFile(): #파일을 저장하기 위한 함수
    f = asksaveasfile(mode = "w", defaultextension= ".txt") #파일 저장을 물어보는 윈도우를 띄워주는 함수
    if f is None:
        return
    ts = str(ta.get(1.0, END))
    f.write(ts) #텍스트 편집기에 저장된 내용을 파일에 쓰고 파일을 닫음
    f.close()

top = Tk()
top.title("메모장")
top.geometry("400x400")

ta= Text(top)

top.grid_rowconfigure(0, weight=1) #텍스트 입력부분 크키에 맞게 윈도우 사이즈 조절
top.grid_columnconfigure(0,weight=1)
ta.grid(sticky = N + E + S +W) #텍스트가 4면을 모두 다 채우도록 고정

file = None #윈도우 크키 설정 아래

mb = Menu(top)
fi = Menu(mb)
mb.add_cascade(label = "파일", menu = fi)
fi.add_command(label = "저장", command = saveFile)

top.config(menu=mb)

top.mainloop()

##김다은##
from tkinter import*

def click(key):
    if key == '=':
        result = eval(display.get())
        s = str(result)
        display.delete(0,END)
        display.insert(END,s)
    elif key == 'C':
        display.delete(0,END)
    else:
        display.insert(END,key)

buttonText = [
    '7','8','9','/','C',
    '4','5','6','*','',
    '1','2','3','-','',
    '0','.','=','+','']

rowlndex = 1
collndex = 0

window = Tk()
window.title("Calculator")

display = Entry(window, width = 33)
display.grid(row = 0, column = 0, columnspan = 5)

for button_Text in buttonText:
    def process(t = button_Text):
        click(t)
    Button(window, text = button_Text, width = 5,
           command = process).grid(row = rowlndex, column = collndex)
    collndex += 1
    if collndex > 4:
        rowlndex += 1
        collndex = 0

window.mainloop()
