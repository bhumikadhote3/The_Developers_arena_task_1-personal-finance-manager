from datetime import datetime

def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                raise ValueError
            return amount
        except ValueError:
            print("❌ Please enter a valid positive number.")

def get_valid_date():
    while True:
        date_input = input("Enter date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("❌ Date must be in YYYY-MM-DD format.")

def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("❌ This field cannot be empty.")
