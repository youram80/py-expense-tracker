expenses = []


def show_average():
    if not expenses:
        print("No expenses recorded.")
        return

    total = sum(item["amount"] for item in expenses)
    average = total / len(expenses)
print(f"Average expense: {average:.2f}")
print("5. Show average")

    elif choice == "5":

         show_average()