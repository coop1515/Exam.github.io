import random

Number = random.randrange(0,3)
player = input("가위 바위 보 중 하나를 내주세요!\n")
print("내가 낸 것 : %s" %player)
if Number == 0:
    computer = "보"
    print("컴퓨터가 낸 것 : %s" %computer)
elif Number == 1:
    computer = "가위"
    print("컴퓨터가 낸 것 : %s" %computer)
else:
    computer = "바위"
    print("컴퓨터가 낸 것 : %s" %computer)


winning = {"가위" : "보", "보" : "바위", "바위" : "가위"}

if not player in winning:
    print("가위 바위 보 중 하나를 내주세요!")

else:
    if computer == player:
        win = 1
        
    elif winning[player] == computer:
        win = 2
    else:
        win = 0

message = ["졌습니다", "비겼습니다", "이겼습니다"]
print (message[win])