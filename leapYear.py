# Write a program to check whether an years is leap year or not.


yr=int(input("Enter the year:-"))
if yr%100==0:
    if yr%400==0:
          print("Entered year is leap year")
    else:
          print("Entered year is not a leap year")
else:
    if yr%4==0:
         print("Entered year is a leap year")  
    else:
        print("Entered year is not a leap year")