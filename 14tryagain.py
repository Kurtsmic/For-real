from datetime import date
f_date = date(input('date 1 :'))
l_date = date(input( 'date 1:'))
delta = l_date - f_date
print(delta.days)