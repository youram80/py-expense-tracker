expenses = []


def show_average():
    if not expenses:
        print("No expenses recorded.")
        return

    total = sum(item["amount"] for item in expenses)
    average = total / len(expenses)
    print(f"Average expense: {average:.2f}")