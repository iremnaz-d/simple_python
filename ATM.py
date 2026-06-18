
balance = 0

def menu(): #prints menu and returns choice
    return str(input("\n1. Check balance\n2. Deposit money\n3. Withdraw money\n0. Exit\n"))


if __name__ == '__main__':
    #global balance

    while True:
        choice = menu()

        if choice not in ["1","2","3","0"]:
            print("Please enter a valid choice")
            continue

        elif choice == "0":
            break

        elif choice == "1":
            print("Current balance is ", balance)

        elif choice == "2":
            balance += int(input("Enter the amount you want to deposit "))

        elif choice == "3":
            amount = int(input("Enter the amount you want to withdraw "))
            if amount > balance:
                print("You are poor")
            else:
                balance -= amount