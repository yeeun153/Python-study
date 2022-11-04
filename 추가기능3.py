from tkinter import*
from tkinter.colorchooser import*
from tkinter.simpledialog import*
from PIL import ImageGrab

mycolor = 'black'

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
    x1,y1=(event.x),(event.y)
    x2,y2=(event.x+2),(event.y-2)
    canvas.create_oval(x1,y1,x2,y2, fill=mycolor)

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

def save(event):#화면 캡쳐 해서 파일에 저장
    x = window.winfo_rootx()
    y = window.winfo_rooty()#창의 위치 얻어오기
    w = window.winfo_width() + x
    h = window.winfo_height() + y#창의 크기 얻어오기

    box = (x, y, w, h)
    img=ImageGrab.grab(box)#창의 크기만큼만 이미지저장
    saveas='손예은_.bmp'
    img.save(saveas)
  
window=None
canvas=None
x1,y1,x2,y2=None,None,None,None #선의 시작점과 끝점
penColor='black' #선의 기본 색-검정
penWidth=5 #선의 기본 굵기-5
fillColor=None
shape="paint"

#if shape=="line":
    
#if shape=="oval":
#if shape=="rectangle":
if __name__=="__main__":
    window=Tk()
    window.title("그림판")
    canvas=Canvas(window,height=850,width=850)

canvas.bind("<Button-1>",mouseClick)
canvas.bind("<ButtonRelease-1>",mouseDrop)
canvas.bind('<B1-Motion>',paint)
canvas.bind("<Button-2>",eraser)
window.bind("<space>", save) #스페이스를 누루면 캡쳐 후 저장
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
fileMenu.add_command(label="지우기",command=eraser)

window.mainloop()
