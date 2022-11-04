#기말프로젝트
from tkinter import*
from tkinter.colorchooser import*
from tkinter.simpledialog import*
from PIL import ImageGrab
import webbrowser
import random

mycolor=["red","yellow","green","blue","black"]
rdcolor=random.choice(mycolor)

def mouseClick(event):
    global x1,y1,x2,y2
    x1=event.x
    y1=event.y

def mouseDrop(event):
    global x1,y1,x2,y2,penWidth,penColor
    x2=event.x
    y2=event.y
    if shape=="line":
        canvas.create_line(x1,y1,x2,y2,width=penWidth,fill=penColor)
    elif shape=="oval":
        canvas.create_oval(x1,y1,x2,y2,width=penWidth,fill=penColor,outline=penColor)
    elif shape=="rectangle":
        canvas.create_rectangle(x1,y1,x2,y2,width=penWidth,fill=penColor,outline=penColor)

def getColor():
    global penColor
    color=askcolor()
    penColor=color[1]

def getWidth():
    global penWidth
    penWidth=askinteger("선 두께","선 두께(1~10)를 입력하세요",minvalue=1,maxvalue=10)

def paint(event):
    x1,y1=(event.x-1),(event.y-1)
    x2,y2=(event.x+1),(event.y+1)
    canvas.create_oval(x1,y1,x2,y2, fill=rdcolor)

def change_color():
    global mycolor
    global rdcolor
    rdcolor=random.choice(mycolor)
    
def drawLine():
    global shape
    shape="line"

def drawOval():
    global shape
    shape="oval"

def drawRectangle():
    global shape
    shape="rectangle"

def eraser():
    canvas.delete("all")

def callback():
    button["text"]="개발자-서울여자대학교 2021111335 손예은"
    
def save(event):
    x = window.winfo_rootx()
    y = window.winfo_rooty() 
    w = window.winfo_width() + x
    h = window.winfo_height() + y

    box = (x, y, w, h)
    img=ImageGrab.grab(box) 
    saveas='손예은_.bmp'
    img.save(saveas)

def quit():
    window.quit()
    window.destroy()
  
window=None
canvas=None
x1,y1,x2,y2=None,None,None,None 
penColor='black' 
penWidth=5 
fillColor=None
shape="paint"

if __name__=="__main__":
    window=Tk()
    window.title("손예은")
    canvas=Canvas(window,height=850,width=850)

url="https://www.naver.com"
def click():
    webbrowser.open(url)
    
canvas.bind("<Button-1>",mouseClick)    
canvas.bind("<ButtonRelease-1>",mouseDrop)
canvas.bind('<Tab>',paint)
canvas.bind("<Button-2>",eraser)
window.bind("<space>", save) 
canvas.pack()

mainMenu=Menu(window)
window.config(menu=mainMenu)

shapeMenu=Menu(mainMenu)
mainMenu.add_cascade(label="모양",menu=shapeMenu)
shapeMenu.add_command(label="선",command=drawLine)
shapeMenu.add_command(label="원",command=drawOval)
shapeMenu.add_command(label="사각형",command=drawRectangle)

fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="설정",menu=fileMenu)
fileMenu.add_command(label="색상 선택",command=getColor)
fileMenu.add_command(label="선 두께 결정",command=getWidth)
fileMenu.add_command(label="change",command=change_color)
fileMenu.add_command(label="지우기",command=eraser)
fileMenu.add_command(label="*저장 시 <space>를 눌러 저장*")

helpMenu=Menu(mainMenu)
mainMenu.add_cascade(label="도움 요청",command=click)

stopMenu=Menu(mainMenu)
mainMenu.add_cascade(label="종료",command=quit)

button=Button(window,text="클릭하시오",command=callback)
button.pack(side=BOTTOM)

window.mainloop()
