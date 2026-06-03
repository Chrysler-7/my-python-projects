
pin = 1054
balance =  10000
print("Welcome to the ATM")

#User input for pin and validation
user_pin = input("Please enter your 4-digit pin:")
#Methods to validate the pin 
if not user_pin.isdigit() and len(user_pin) != 4:
    print("Invalid pin format. Please enter a numeric 4-digit pin.")
else:
    if int(user_pin) != pin:
       print("Incorrect pin. Access denied.")
    else:
       print("""
       1. Check Balance
       2. Deposit Cash
       3. Withdraw Cash
             """)
    choice = input("Please select an option (1, 2, or 3): ")
#Handling user choices
    if choice == "1":
        print(f"Your current balance is: ${balance}")
    elif choice == "2":
        deposit_amount = input("Enter deposit amount:")
        if deposit_amount.isdigit():
            balance += int(deposit_amount)
            print(f"Deposit successful. New balance: ${balance}")
        else:
            print("Invalid amount.")
    elif choice == "3":
        withdrawal_amount = input("Enter withdrwal amount:")
        if withdrawal_amount.isdigit():
            if int(withdrawal_amount) > balance:
                print("Insufficient funds.")
            else:
                balance -= int(withdrawal_amount)
                print(f"Withdrawal successful. New balance: ${balance}") 
    else:
        print("Invalid option selected.")

    


   



   
