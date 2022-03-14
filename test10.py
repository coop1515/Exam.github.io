from tkinter import *
import random
from tkinter import messagebox

Result = Tk()
a = random.randint(1, 10)
b = random.randint(1,10)
c = random.randint(1, 3)
if a>b:
    if c == 1:
        c = "-"
        d = a - b
    else:
        c = "+"
        d = a + b
else:
    if c == 1:
        c = "-"
        d = b - a
    else:
        c = "+"
        d = a + b
count = 0

def suit():

    a = random.randint(1, 10)
    b = random.randint(1,10)
    c = random.randint(1, 3)
    en1.delete(0,10)
    en2.delete(0,10)

    if a > b:
        if c == 1:
            c = "-"
            d = a - b
        else:
            c = "+"
            d = a + b
    else:
       return suit()
    if a>b:
        en1.insert(10,("%d"%a,"%s"%c,"%d"%b))
        print("%d"%a,"%s"%c,"%d ? "%b)
        print("%d"%d)
    else:
        en1.insert(10,("%d"%b,"%s"%c,"%d"%a))
        print("%d"%b,"%s"%c,"%d ? "%a)
        print("%d"%d)
    
    
    if d == int(en2.get()):
       
        #Acces = Tk()
        #lb1 = Label(Acces, text = "You got it")
        #lb1.grid(row=1,column =1)
        messagebox.showinfo("messagebox","you got it!")
        
    else:
       return
    
def search():
    if d == int(en2.get()):
        
        #Acces = Tk()
        #lb1 = Label(Acces, text = "You got it")
        #lb1.grid(row=1,column =1)
        messagebox.showinfo("messagebox","you got it!")
        return suit()
    



en1 = Entry(Result)
en2 = Entry(Result)
en1.grid(row=0, column =1)
en2.grid(row=1, column =1)
if a>b:
    en1.insert(10,("%d"%a,"%s"%c,"%d"%b))
else:
    en1.insert(10,("%d"%b,"%s"%c,"%d"%a))


bt1 = Button(Result, width = 10, text="Enter", command=search)
bt1.grid(row=2, column=2)
lb1 = Label(Result, text = " 맞춘 횟수 %d"%count)
lb1.grid(row=1, column=2)


Result.mainloop()