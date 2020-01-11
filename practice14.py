import datetime 
x = input('day first :')
y = input('day second:')
dx = datetime.datetime.strptime(x, '%Y-%m-%d')
dy = datetime.datetime.strptime(y, '%Y-%m-%d')
delta = dy - dx
print(delta)