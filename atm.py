class ATM:
    def __init__(self, balance=0, pin=1234):
        # Initialize the ATM with a default balance and PIN
        self.balance = balance
        self.pin = pin
        self.transaction_history = []

    def login(self, card_number, pin):
        # Verify the PIN to allow access to the ATM's functions
        if pin == self.pin:
            print("Login successful!")
            return True
        else:
            print("Invalid PIN. Please try again.")
            return False

    def check_balance(self):
        # Display the current account balance
        print(f"Your account balance is: ${self.balance}")

    def withdraw(self, amount):
        # Allow cash withdrawal if the account balance is sufficient
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: -${amount}")
            print(f"Withdrawal successful! New balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def deposit(self, amount):
        # Deposit cash into the account
        self.balance += amount
        self.transaction_history.append(f"Deposit: +${amount}")
        print(f"Deposit successful! New balance: ${self.balance}")

    def change_pin(self, old_pin, new_pin):
        # Securely update the PIN
        if old_pin == self.pin:
            self.pin = new_pin
            print("PIN changed successfully!")
        else:
            print("Invalid old PIN. Please try again.")

    def transaction_history(self):
        # Display the list of recent transactions
        for transaction in self.transaction_history:
            print(transaction)


def main():
    # Initialize the ATM with an initial balance
    atm = ATM(balance=1000)

    while True:
        # Display the main menu
        print("Welcome to Your Bank's ATM")
        print("1. Login")
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            card_number = input("Enter your card number: ")
            pin = int(input("Enter your PIN: "))

            # Attempt to log in
            if atm.login(card_number, pin):
                while True:
                    # Display the ATM menu
                    print("1. Account Balance")
                    print("2. Cash Withdrawal")
                    print("3. Cash Deposit")
                    print("4. PIN Change")
                    print("5. Transaction History")
                    print("6. Exit")

                    option = input("Choose an option: ")

                    if option == "1":
                        # Check account balance
                        atm.check_balance()
                    elif option == "2":
                        # Withdraw cash
                        amount = float(input("Enter withdrawal amount: "))
                        atm.withdraw(amount)
                    elif option == "3":
                        # Deposit cash
                        amount = float(input("Enter deposit amount: "))
                        atm.deposit(amount)
                    elif option == "4":
                        # Change PIN
                        old_pin = int(input("Enter old PIN: "))
                        new_pin = int(input("Enter new PIN: "))
                        atm.change_pin(old_pin, new_pin)
                    elif option == "5":
                        # View transaction history
                        atm.transaction_history()
                    elif option == "6":
                        # Exit the ATM
                        break
                    else:
                        print("Invalid option. Please try again.")
            else:
                continue
        elif choice == "2":
            # Exit the program
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()

