from tkinter import *
import random

Game = Tk()

Game.title("가위바위보")

button_list = ["Rock", "Paper", "Scissors"]

RockImage = PhotoImage(file="바위.png")
PaperImage = PhotoImage(file="보.png")
ScissorImage = PhotoImage(file="가위.png")
label1 = Label(Game, image = PaperImage)
label2 = Label(Game, image = PaperImage)
label1.grid(row = 0, column=0)
label2.grid(row = 0, column=2)
label3 = Label(Game, text = "사용자")
label3.grid(row = 1, column = 0)
label4 = Label(Game, text = "컴퓨터")
label4.grid(row = 1, column = 2)
def update_image(num, Img):
    if num == 1:
        inputLabel_1 = Label(Game,image=Img)
        inputLabel_1.grid(row=0, column=0)
    elif num == 2:
        inputLabel_2 = Label(Game,image=Img)
        inputLabel_2.grid(row=0,column=2)


def play(choice):
    opponent = random.randint(1, 3)
    if opponent == 1:
        update_image(2, RockImage)
    elif opponent == 2:
        update_image(2, PaperImage)
    elif opponent == 3:
        update_image(2, ScissorImage)

    if choice == 1:
        update_image(1, RockImage)
    elif choice == 2:
        update_image(1, PaperImage)
    elif choice == 3:
        update_image(1, ScissorImage)

    if (choice, opponent) in [(1, 2), (2, 3), (3, 1)]:
        
        ResultLabel = Label(Game, width=10, text="컴퓨터 승 !", fg="red")
        result = 1
    elif (choice, opponent) in [(1, 3), (2, 1), (3, 2)]:
        
        ResultLabel = Label(Game, width=10, text="사용자 승!", fg="green")
        result = -1
    else:
        
        ResultLabel = Label(Game, width=10, text="비겼습니다 !", fg="Blue")
        result = 0

    
    ResultLabel.grid(row=0, column=1)
    return result


for i, button_text in enumerate(button_list):

    def click(t=i):
        play(t + 1)

    Button(Game, text=button_text, width=30, command=click).grid(row=2, column=i)

Game.mainloop()
