def main():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    college = input("Enter your college name: ")
    print(f"Name: {name}, Age: {age}, College: {college}")

    with open("student.txt", "w") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"College: {college}\n")

    print("\nInformation saved to student.txt")

if __name__ == "__main__":
    main()    
