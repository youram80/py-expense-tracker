expenses = []


def show_average():
    if not expenses:
        print("No expenses recorded.")
        return

    total = sum(item["amount"] for item in expenses)
    average = total / len(expenses)
    print(f"Average expense: {average:.2f}")


def main():
    while True:
        print("5. show average")
        choice = input("Choice: ")
        if choice == "0":
            break
        elif choice == "5":
            show_average()


if __name__ == "__main__":
    main()