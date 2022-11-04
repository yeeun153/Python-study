from tkinter import*
from PIL import ImageGrab

window = None
canvas = None
x1, y1 = None, None #start Point

def mouseMove(event):
  global x1, y1
  x1 = event.x
  y1 = event.y
  canvas.create_line(x1, y1, x1+5, y1+5, width=5, fill="black") #글자색

def save(event):#화면 캡쳐 해서 파일에 저장
    x = window.winfo_rootx()
    y = window.winfo_rooty()#창의 위치 얻어오기
    w = window.winfo_width() + x
    h = window.winfo_height() + y#창의 크기 얻어오기

    box = (x, y, w, h)
    img=ImageGrab.grab(box)#창의 크기만큼만 이미지저장
    saveas='ScreenShot_.bmp'
    img.save(saveas)

window=Tk()
window.title("파이썬 그림판")
canvas=Canvas(window, height=850, width=850)
window.bind("<B1-Motion>", mouseMove)
window.bind("<space>", save)#스페이스를 누루면 캡쳐쳐

canvas.pack()
window.mainloop()

from PIL import ImageTk, Image, ImageDraw
import PIL
from tkinter import*

width=500
height=500
white=(255,255,255)
green=(0,128,0)

def save():
    name="rimage.png"
    image1.save(name)
def save():#화면 캡쳐 해서 파일에 저장
    x = window.winfo_rootx()
    y = window.winfo_rooty()#창의 위치 얻어오기
    w = window.winfo_width() + x
    h = window.winfo_height() + y#창의 크기 얻어오
def paint(event):
    x1,y1=(event.x-1),(event.y-1)
    x2,y2=(event.x+1),(event.y+1)
    canvas.create_oval([x1,y1,x2,y2],fill="black",width=5)
    draw.line((x1,y1,x2,y2), fill="black", width=10)

window=Tk()

canvas=Canvas(window,width=width,height=height,bg="white")
canvas.pack()

image1=PIL.Image.new("RGB",(width,height),(255,255,255))
draw=ImageDraw.Draw(image1)


canvas.bind("<B1-Motion>",paint)

b1=Button(text="저장",command=save)
b1.pack()
window.mainloop()
