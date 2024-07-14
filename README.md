#ATM Simulator

Welcome to the ATM Simulator repository! This project is a simple ATM simulator written in Python. It allows users to perform basic ATM operations like checking their balance, depositing money, withdrawing money, and exiting the program.

Features:

     Check Balance: View the current balance.
     Deposit Money: Add money to the balance.
     Withdraw Money: Withdraw money from the balance (with insufficient funds check).
     Exit Program: Exit the ATM simulator.

Installation

  Clone the repository:

        sh
        git clone https://github.com/yourusername/atm-simulator.git
        
  Navigate to the project directory:

        sh

        cd atm-simulator

  Usage
  
  To run the ATM simulator, execute the atm_simulator.py file:

       sh

       python atm_simulator.py

Example Output : ->

      Welcome to the ATM simulator

     Menu:
     1. Check Balance
     2. Deposit
     3. Withdraw
     4. Exit
     Enter your choice (1-4): 1
     Your balance is: $1000

    Menu:
    1. Check Balance
    2. Deposit
    3. Withdraw
    4. Exit
    Enter your choice (1-4): 2
    Enter amount to deposit: $200
    Deposit successful. New balance: 1200.0

    Menu:
    1. Check Balance
    2. Deposit
    3. Withdraw
    4. Exit
    Enter your choice (1-4): 3
    Enter amount to withdraw: $500
    Withdrawal successful. New balance: 700.0

    Menu:
    1. Check Balance
    2. Deposit
    3. Withdraw
    4. Exit
    Enter your choice (1-4): 3
    Enter amount to withdraw: $800
    Insufficient funds

    Menu:
    1. Check Balance
    2. Deposit
    3. Withdraw
    4. Exit
    Enter your choice (1-4): 4
    Thank you for using the ATM. Goodbye!

    
source Code : 


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


    
