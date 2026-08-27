numbers = [1, 2, 2, 3, 3, 3, 4]
def count_occurence(numbers):
    occurence_dict = {}
    for number in numbers:
        if number in occurence_dict:
            occurence_dict[number] += 1
        else:
            occurence_dict[number] = 1
    return occurence_dict

print(count_occurence(numbers))