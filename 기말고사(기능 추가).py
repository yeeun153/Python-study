from tkinter import*
from tkinter.simpledialog import*
import tkinter as tk
from tkinter import filedialog
from tkinter import filedialog as fd
from tkinter.colorchooser import*
from PIL import ImageGrab
from PIL import Image,ImageDraw


def mouseClick(event):
    global x1,y1,x2,y2
    x1=event.x
    y1=event.y

def mouseDrop(event):
    global x1,y1,x2,y2,penWidth,penColor,shape
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
    ##global x1,y1
    ##x1=event.x
    ##y1=event.y
    ##canvas.create_line(x1,y1,x1+1,y1+1,width=penWidth,fill="black")
    canvas.delete("all")

def save():
    
    saveIm=filedialog.asksaveasfile(parent=window, mode="w", defaultextension=".png", filetypes=(("png파일", "*.png"),("모든 파일", ".")))
    canvas.save(filename=saveIm.name)

    '''x=window.winfo_rootx()  #창의 왼쪽 위의 x 좌표
    y=window.winfo_rooty()  #창의 왼쪽 위의 y 좌표
    w = window.winfo_width() + x  
    h = window.winfo_height() + y
    box = (x, y, w, h)
    img=ImageGrab.grab(box)
    filename=filedialog.asksaveasfile(parent=window,mode="w",initialdir="/",title="Select file",filetypes=(("png files","*.png"),("all files","*.*")))
    img.save(filename)'''

    
def quit():
    window.quit()
    window.destroy()

window=None
canvas=None
x1,y1,x2,y2=None,None,None,None #선의 시작점과 끝점
penColor='black' #선의 기본 색-검정
penWidth=5 #선의 기본 굵기-5
fillColor=None
shape="line"

if __name__=="__main__":
    window=Tk()
    window.title("그림판")
    canvas=Canvas(window,height=300,width=300)
    

canvas.bind("<Button-1>",mouseClick)
canvas.bind("<ButtonRelease-1>",mouseDrop)
canvas.bind("<Button-2>",eraser)
window.bind("<space>",save)

canvas.pack()

                     

mainMenu=Menu(window)
window.config(menu=mainMenu)
saveMenu=tk.Menu(window)

shapeMenu=Menu(mainMenu)
mainMenu.add_cascade(label="모양",menu=shapeMenu)
shapeMenu.add_command(label="선",command=drawLine)
shapeMenu.add_command(label="원",command=drawOval)
shapeMenu.add_command(label="사각형",command=drawRectangle)

fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="설정",menu=fileMenu)
fileMenu.add_command(label="색상 선택",command=getColor)
fileMenu.add_command(label="선 두께 결정",command=getWidth)
fileMenu.add_command(label="지우기",command=eraser)


saveMenu=Menu(mainMenu)
mainMenu.add_cascade(label="저장",menu=saveMenu)
saveMenu.add_command(label="저장",command=save)
saveMenu.add_command(label="다른 이름으로 저장",command=save)
saveMenu.add_command(label="끝내기",command=quit)

window.mainloop()
