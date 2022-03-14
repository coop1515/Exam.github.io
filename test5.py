import turtle

t = turtle.Turtle()
t.shape("circle")
t.left(108)
#for i in range(5):
#    t.circle(100 ,steps = 5)
#    t.left(72)
for i in range(5):
    t.circle(100, steps=5)
    for j in range(1):
        t.left(72)
#for i in range(1,6):
#    print(" "*(5-i), end="")
#    print("*"*(2*i-1))
for i in range(1,6):
    print(" "*(5-i), end="")
    for j in range(1):
        print("*"*(2*i-1))