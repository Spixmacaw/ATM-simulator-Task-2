# atm simulation for deposite and withdrow,exit 
class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit successful. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return f"Withdrawal successful. New balance: {self.balance}"


# Example usage
if __name__ == "__main__":
    atm = ATM(1000)  # Initialize ATM with $1000 balance

    print("Welcome to the ATM simulator")
    while True:
        print("\nMenu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print(f"Your balance is: ${atm.check_balance()}")

        elif choice == "2":
            amount = float(input("Enter amount to deposit: $"))
            print(atm.deposit(amount))

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: $"))
            print(atm.withdraw(amount))

        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
