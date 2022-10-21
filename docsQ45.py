days=int(input('enter no of days:-'))
if days<=5:
    print(days*2)
elif days>5 and days<=10:
    a=(days-5)*3
    print(5*2+a)
elif days>10 and days<=15:
    a=(days-10)*4
    print(5*2+5*3+a)
else:
    a=(days-15)*5
    print(5*2+5*3+5*4+a)