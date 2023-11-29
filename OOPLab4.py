from tkinter import *
root = Tk()
root.title("My Gui")
# กำหนดขนาดหน้าจอ
root.geometry("500x400")


# #หน้าจอหน้าที่2
# Mywindow = Tk()
# Mywindow.title("Report!")
# Mywindow.geometry("500x400")

# ใส่ข้อความในหน้าจอ
# กำหนดตำแหน่งแบบแกนX,Y
# myLabel = Label(Mywindow,text = "Fuck you",bg="sky blue").place(x=0,y=0)

def showmessage():
    message = txt.get()
    myLabel5 = Label(root, text="Hello Stupid Boys " +
                     message, fg="#FF00FF", font=50).pack()


def openwindows():
    Mywindow = Tk()
    Mywindow.title("Report!")
    Mywindow.geometry("500x400")


# กล่องข้อความ
txt = StringVar()
myText = Entry(root, textvariable=txt).pack()


# ปุ่ม
bt1 = Button(text="Ok", bg="pink", command=showmessage).pack()
bt2 = Button(text="Exit", bg="red", command=openwindows).pack()


root.mainloop()
