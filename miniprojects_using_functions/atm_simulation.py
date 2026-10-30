balance = 10000
def show_menu():
    print("\nATM Options")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

def check_balance():
    print(f"Available Balance: {balance}")

def deposit():
    global balance
    amount = int(input("Enter the amount to deposit: "))
    if amount <= 0:
        print("Error: Please enter an amount greater than 0")
    else:
        balance += amount
        print(f"Amount deposited: {amount}")
        print(f"Available Balance: {balance}")

def withdrawl():
    global balance
    amount = int(input("Enter the amount to withdraw: "))
    if amount <= 0:
        print("Error: Enter an amount greater than 0")
    elif amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
        print(f"Amount withdrawn: {amount}")
        print(f"Available Balance: {balance}")

while True:
    show_menu()
    option = int(input("Select an option: "))
    if option == 1:
        check_balance()
    elif option == 2:
        deposit()
    elif option == 3:
        withdrawl()
    elif option == 4:
        print("Thank you for using our ATM!")
        break
    else:
        print("Invalid option")
