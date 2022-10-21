unit=int(input('enter units:-'))
if unit<=100:
    print('free')
elif unit>100 and unit<=200:
    print((unit-100)*5)
elif unit>200:
    amt=(100*5)+(unit-200)*10
    print(amt)
