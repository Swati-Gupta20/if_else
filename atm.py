#  ATM Question

balance=50000
pincode=4321
print("welcome to Punjab National Bank")
print("insert your card")
pin=int(input("enter your pin"))
if pin==pincode:
    print("1 = withdraw")
    print("2 = check_balance")
    print("3 = deposit")
    transaction=input("select any service")
    if transaction=="1":
        withdraw_amt=int(input("enter amount"))
        if withdraw_amt<=balance:
            print("processing")
            print("collect your cash",withdraw_amt)
            print("your current balance:",balance-withdraw_amt)
            print("thanks for visiting")
        else:
            print("insufficient amount")
    elif transaction=="2":
        print("your current balance is",balance)
    elif transaction=="3":
        deposit_amt=int(input("enter amount"))
        print("your amount is successfully deposit")
        print("your current balance is ",balance+deposit_amt)
else:
    print("wrong pin_code")
    
    
    







