FILENAME = "expenses.txt"


def add_expense():
    item = input("Enter expense item name: ").strip()
    try:
        amount = float(input("Enter amount ($): "))
    except ValueError:
        print("Invalid amount! Please enter a valid number.\n")
        return

    
    with open(FILENAME, "a") as file:
        file.write(f"{item},{amount}\n")

    print(f"Added: {item} - ${amount:.2f}\n")


def view_expenses():
    try:
        with open(FILENAME, "r") as file:
            lines = file.readlines()

        if not lines:
            print("\nNo expenses logged yet.\n")
            return

        print("\n--- Expense List ---")
        for index, line in enumerate(lines, start=1):
            item, amount = line.strip().split(",")
            print(f"{index}. {item}: ${float(amount):.2f}")
        print("---------------------\n")

    except FileNotFoundError:
        print("\nNo expense records found. Add an expense first!\n")


def calculate_total():
    try:
        total = 0.0
        with open(FILENAME, "r") as file:
            for line in file:
                _, amount = line.strip().split(",")
                total += float(amount)

        print(f"\nTotal Spending: ${total:.2f}\n")

    except FileNotFoundError:
        print("\nNo expense records found. Total is $0.00\n")


def main():
    while True:
        print("=== EXPENSE TRACKER ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    main()