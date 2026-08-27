numbers = [10, 25, 5, 40, 15]
def find_min(numbers):
    min_number = numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number
    return min_number
print(find_min(numbers))