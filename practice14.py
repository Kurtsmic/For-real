from datetime import date
x = int(input('day first :'))
y = int(input('day second:'))
datetime(x, '%Y, %m, %d')
datetime(y, '%Y, %m, %d')
delta = (y - x)
print(delta)