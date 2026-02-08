import csv
from expense import Expense

FILE_NAME = "data/expenses.csv"

def save_expenses(expenses):
    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])
        for expense in expenses:
            writer.writerow([expense.date, expense.category, expense.amount, expense.description])

def load_expenses():
    expenses = []
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expense = Expense(
                    row["Amount"],
                    row["Category"],
                    row["Date"],
                    row["Description"]
                )
                expenses.append(expense)
    except FileNotFoundError:
        pass
    return expenses
