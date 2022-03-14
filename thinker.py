from tkinter import *  #Tk
#root = Tk()
#root.mainloop()

top = Tk()

top.title("BMI 계산")
lb1 = Label(top, text = "키(m)")
lb2 = Label(top, text = "BMI")
lb3 = Label(top, text = "몸무게(Kg)")
lb4 = Label(top)

lb1.grid(row = 0, column=0)
lb2.grid(row = 0, column=2)
lb3.grid(row = 1, column=0)
lb4.grid(row = 1, column=2)

en1 = Entry(top)
en2 = Entry(top)
en1.grid(row=0, column =1)
en2.grid(row=1, column =1)

def calc():
    height =  float(en1.get())
    weight = float(en2.get())
    bmi = weight / height **2
    lb4["text"] = str(bmi)

bt1 = Button(top, width = 10, text="계 산", command=calc)
bt1.grid(row=2, column=2)

top.mainloop()
