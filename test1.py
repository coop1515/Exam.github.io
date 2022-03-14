a, b = input("투입한 돈, 물건값 : ").split(',')
c = int(a) - int(b)
d = c // 500
e = (c - (d*500)) // 100
print ("거스름돈 : %d " %c)
print ("500원 동전의 개수 : %d" %d)
print ("100원 동전의 개수 : %d" %e)