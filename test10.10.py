from tkinter import *
import random
from tkinter import messagebox
w=Tk()

cnt=0
def enter():
    a=int(en2.get())
    b=int(en3.get())
    global cnt
    if a==b:
        cnt+=1
        messagebox.showinfo("messagebox","you got it!  맞힌 수 "+str(int(cnt)))
        en1.delete(0,END)
        en2.delete(0,END)
        en3.delete(0,END)
        
        n1=random.randrange(0,101)
        n2=random.randrange(0,101)
        ran=random.randint(1,2)
        if ran==1:
            s=n1+n2
            en1.insert(0,str(n1)+"+"+str(n2))
            en2.insert(0,s)
        elif ran==2:
            if n1<n2:
                n3=n1
                n1=n2
                n2=n3
            s=n1-n2
            en1.insert(0,str(n1)+"-"+str(n2))
            en2.insert(0,s)

    
lb1= Label(w, text='입력').pack()
en1=Entry(w)
en1.pack()
en2=Entry(w)
en2.pack()
en3=Entry(w)
en3.pack()

n1=random.randrange(0,101)
n2=random.randrange(0,101)
ran=random.randint(1,2)
if ran==1:
    s=n1+n2
    en1.insert(0,str(n1)+"+"+str(n2))
    en2.insert(0,s)
elif ran==2:
    if n1<n2:
        n3=n1
        n1=n2
        n2=n3
        
    s=n1-n2
    en1.insert(0,str(n1)+"-"+str(n2))
    en2.insert(0,s)
    
        
bt1=Button(w,width=10,text="enter",command=enter)
bt1.pack()

w.mainloop()