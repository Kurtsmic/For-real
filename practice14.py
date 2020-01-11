import datetime as DT
x = input('day first :')
y = input('day second:')
dx = DT.datetime.strptime(x, '%Y-%m-%d')
dy = DT.datetime.strptime(y, '%Y-%m-%d')
delta = dy - dx
print(delta)