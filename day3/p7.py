def calculate(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total
print(calculate(1,2))
print(calculate(1,2,5))
print(calculate(1,2,5,4,5,4))
