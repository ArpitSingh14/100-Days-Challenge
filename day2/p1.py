Correct_Pin = 1234
Balance = 10000

Pin = eval(input("Enter you pin:"))
if Pin == Correct_Pin:
    print("welcome")

    while True:
        print("---------Menu----------")
        print("1.Check Balance")
        print("2.Deposit")
        print("3.withdrawl")
        print("4.Exit")

        choice = eval(input("Enter your choice: "))

        if choice == 1:
            print("your balance is ₹",Balance)

        elif choice == 2:
            amount = eval(input("enter the amount to deposit: ")) 
            Balance += amount
            print("------Amount deposited successfully-------")
            print("updated balance is:",Balance)

        elif choice == 3:
            amount = eval(input("Enter the amount you want to withdrawl: "))
            if amount <= Balance:
                Balance -= amount
                print("remaining balance is",Balance)
            else:
                print("insufficient balance")
        elif choice == 4:
            print("Thank you for using ATM")
            break

        else:
            print("Invalid choice")   
else:
    print("incorrect pin")

