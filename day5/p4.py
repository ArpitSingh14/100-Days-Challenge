numbers = [1, 2, 2, 3, 4, 4, 5]
def unique_numbers(numbers):
    unique_list = []
    for number in numbers:
        if number not in unique_list:
            unique_list.append(number)
    return unique_list
print(unique_numbers(numbers))