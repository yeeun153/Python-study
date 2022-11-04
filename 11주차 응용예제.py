#응용예제
#강의자료의 사진을 첨부하여 이미지 압축파일은 제출하지 않았습니다.
from tkinter import*
window = Tk()
window.geometry("400x400")
window.title("반려동물 선택하기")


label1 = Label(window, text = "좋아하는 동물 투표", font = ("궁서체", 30), fg = "blue")

def myFunc() :
        if var.get() == 1:
            label2.configure(image = photo1)
           
        elif var.get() == 2:
            label2.configure(image = photo2)
        elif var.get()==3:
            label2.configure(image = photo3)
        else:
            label2.configure(image=photo4)
  
button = Button(window, text = "사진보기", command = myFunc)   
label2 = Label(window, bg = "yellow", width = 200, height = 200, image = None)

var = IntVar()
rb1 = Radiobutton(window,text = "강아지", variable = var, value = 1)
rb2 = Radiobutton(window,text = "고양이", variable = var, value = 2)
rb3 = Radiobutton(window,text = "토끼", variable = var, value = 3)
rb4 = Radiobutton(window,text = "말", variable = var, value = 4)

photo1 = PhotoImage(file = "gif/dog.gif")
photo2 = PhotoImage(file = "gif/cat2.gif")
photo3 = PhotoImage(file = "gif/rabbit.gif")
photo4 = PhotoImage(file = "gif/horse.png")
    
label1.pack()
rb1.pack()
rb2.pack()
rb3.pack()
rb4.pack()
button.pack()
label2.pack()
window.mainloop()
