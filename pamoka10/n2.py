# Write a function that takes a list of numbers as input and returns:
# The sum of all numbers in the list.
# A new list with each element squared
# [1, 2, 3, 4]  -> (10, [1, 4, 9, 16])


def process_numbers(numbers: list) -> tuple:
    square_list = []
    sum = 0
    for i in  numbers:
        sum += i
        square_list.append(i * i)
    
    return sum, square_list

print(process_numbers([1, 2, 3, 8]))


 

 

