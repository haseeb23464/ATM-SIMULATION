balence = 100000000000000000
pin = 1234
print("Welcome to the ATM")
entered_pin = int(input("Please enter your PIN: "))
if pin in [entered_pin]:
    print("PIN accepted")
    while True:
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(f"Your balance is: ${balence}")
        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balence:
                balence -= amount
                print(f"Please collect your cash. New balance is: ${balence}")
            else:
                print("Insufficient balance.")
        elif choice == 3:
            amount = float(input("Enter amount to deposit: "))
            balence += amount
            print(f"Amount deposited successfully. New balance is: ${balence}")
        elif choice == 4:
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")