side1=input("enter a number:-")
side2=input("enter a number:-")
side3=input("enter a number:-")
if side1==side2 and side2==side3 and side3==side1:
    print("Equaleteral triangle")
elif side1==side2 or side2==side3 or side3==side1:
    print("isosceles triangle")
else:
    print("scalene triangle" )
