try:
    file = open("data.txt")
    print(file.read())

except FileNotFoundError:
    print("File doesn't exist.")

finally:
    print("Operation completed.")