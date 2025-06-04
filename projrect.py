class Bank_Account:
    def __init__(self):
        self.balance =200
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
def login(self, account_number, password):
        if account_number not in self.accounts:
            print("Account does not exist.")
            return False
        if self.accounts[account_number].password == password:
            print("Login successful.")
            return True
        else:
            print("Invalid password.")
            return False

def deposit(self):
    amount = float(input("Enter amount to be Deposited: "))
    self.balance += amount
    print("\n Amount Deposited:", amount)

def withdraw(self):
    amount = float(input("Enter amount to be Withdrawn: "))
    if self.balance >= amount:
        self.balance -= amount
        print("\n You Withdrew:", amount)
    else:
        print("\n Insufficient balance  ")

def display(self):
        print("\n Net Available Balance=", self.balance)
while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        s.deposit()
    elif choice == "2":
        s.withdraw()
    elif choice == "3":
        s.display()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")  