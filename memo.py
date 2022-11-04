#Step 1~3
from tkinter import*
from tkinter.filedialog import*
import os

def saveFile():
    f=asksaveasfile(mode="w",defaultextension=".txt") #defaultextension;확장자
    if f is None:
        return
    ts=str(ta.get(1.0,END))
    f.write(ts)
    f.close()

top=Tk()
top.title("메모장")
top.geometry("400x400")

ta=Text(top)
top.grid_rowconfigure(0,weight=1)
top.grid_columnconfigure(0,weight=1)
ta.grid(sticky=N+E+S+W)

file=None

mb=Menu(top) #Menu라는 top이라는 윈도우에 포함
fi=Menu(mb)
mb.add_cascade(label="파일",menu=fi)
fi.add_command(label="저장",command=saveFile)

top.config(menu=mb)

top.mainloop()


