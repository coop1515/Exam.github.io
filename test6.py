def d2x(a,b):
    if a == 0:
        return
    else:
        d2x(a//b,b)
        print(a%b,end="")
d2x(10,3 ) #a에 들어갈 10진수를 b진수로 바꾸는것
#print("")
#d2x(10,3)
#print("")     
#d2x(10,8)

