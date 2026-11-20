def delete_expense():
    if not expenses:
        print("No expenses to delete.")
        return

    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['description']}")

    choice = input("Expense number to delete: ")
    if not choice.isdigit():
        print("Invalid expense number.")
        return

    index = int(choice) - 1
    if 0 <= index < len(expenses):
        removed = expenses.pop(index)
        print(f"Deleted: {removed['description']}")
    else:
        print("Invalid expense number.")