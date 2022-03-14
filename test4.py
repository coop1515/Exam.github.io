import math



def points(x,y,a,b):
    x = int(x)
    y = int(y)
    a = int(a)
    b = int(b)
    st = x - a
    height = y - b
    dis = str(math.sqrt(st**2 + height**2))
    if height == 0:
        gra = str("infinity")
    else:
        gra = str(height / st)
    print("The slope is %s" %gra, " and distance is %s" %dis)

x,y,a,b = input("숫자를 입력하세요 : ").split(',')
points(x,y,a,b)
