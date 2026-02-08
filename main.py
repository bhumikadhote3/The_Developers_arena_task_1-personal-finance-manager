from expense import Expense
from file_manager import save_expenses, load_expenses
from menu import show_menu
from reports import total_expenses, category_summary
from utils import get_valid_amount, get_valid_date, get_non_empty_input

expenses = load_expenses()

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        amount = get_valid_amount()
        category = get_non_empty_input("Enter category: ")
        date = get_valid_date()
        description = get_non_empty_input("Enter description: ")

        expense = Expense(amount, category, date, description)
        expenses.append(expense)
        save_expenses(expenses)
        print("✅ Expense added successfully!")

    elif choice == "2":
        print("\nAll Expenses:")
        if not expenses:
            print("No expenses found.")
        else:
            for exp in expenses:
                print(exp)

    elif choice == "3":
        print("\n📊 SUMMARY REPORT")
        print("-------------------")
        print(f"Total Expenses: ₹{total_expenses(expenses)}")
        summary = category_summary(expenses)
        for cat, amt in summary.items():
            print(f"{cat}: ₹{amt}")

    elif choice == "4":
        print("👋 Exiting... Goodbye!")
        break

    else:
        print("❌ Invalid choice. Try again.")
