numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def even(numbers):
    even_list =[]
    for number in numbers:
        if number%2==0:
            even_list.append(number)
    return even_list
print(even(numbers))