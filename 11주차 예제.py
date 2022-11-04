#Code10-17
from tkinter import*

window=Tk()

mainMenu=Menu(window)
window.config(menu=mainMenu)

fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="파일",menu=fileMenu)
fileMenu.add_command(label="열기")
fileMenu.add_separator()
fileMenu.add_command(label="종료")

window.mainloop()

#Code10-18
from tkinter import*
from tkinter import messagebox

def func_open():
    messagebox.showinfo("메뉴선택","열기 메뉴를 선택함")

def func_exit():
    window.quit()
    window.destroy()

window=Tk()

mainMenu=Menu(window)
window.config(menu=mainMenu)

fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="파일",menu=fileMenu)
fileMenu.add_command(label="열기",command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="종료",command=func_exit)

window.mainloop()

#Code10-19
from tkinter import*
from tkinter.simpledialog import*

window=Tk()
window.geometry("400x100")

label1=Label(window,text="입력된 값")
label1.pack()

value=askinteger("확대배수","주사위 숫자(1~6)을 입력하세요",minvalue=1,maxvalue=6)

label1.configure(text=str(value))
window.mainloop()

##Code10-19-이름출력
from tkinter import*
from tkinter.simpledialog import*

window=Tk()
window.geometry("400x100")

label1=Label(window,text="입력된 값")
label1.pack()

value=askstring("이름","이름을 입력하세요")

label1.configure(text=str(value))
window.mainloop()


#Code10-20
from tkinter import*
from tkinter.filedialog import*

window=Tk()
window.geometry("400x100")

label1=Label(window,text="선택된 파일 이름")
label1.pack()

filename=askopenfile(parent=window,filetypes=(("GIF 파일","*.gif"),("모든 파일","*.*")))

label1.configure(text=str(filename))

window.mainloop()

#Code10-21
from tkinter import*
from tkinter.filedialog import*

window=Tk()
window.geometry("400x100")

label1=Label(window,text="선택된 파일 이름")
label1.pack()

saveFp=asksaveasfile(parent=window,mode="w",defaultextension=".jpg",filetypes=(("JPG 파일","*.jpg;*.jpeg"),("모든 파일","*.*")))
label1.configure(text=saveFp)
saveFp.close()

window.mainloop()

#Code10-22
from tkinter import*
from tkinter.filedialog import*

def func_open():
    filename=askopenfilename(parent=window,filetypes=(("GIF 파일","*.gif"),("모든 파일","*.*")))
    photo=PhotoImage(file=filename)
    pLabel.configure(image=filename)
    pLabel.image=photo

def func_exit():
    window.quit()
    window.destroy()

window=Tk()
window.geometry("400x400")
window.title("영화 감상하기")

photo=PhotoImage()
pLabel=Label(window,image=photo)
pLabel.pack(expand=1,anchor=CENTER)

mainMenu=Menu(window)
window.config(menu=mainMenu)
fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="파일",menu=fileMenu)
fileMenu.add_command(label="파일 열기",command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료",command=func_exit)

window.mainloop()
