# my_list = [1, 2, 3, 4, 5]

# a = 2

# my_dictionary = {"Antanas": 1, "Jonas": 2, "Petras": 3}

# print(my_dictionary)


# print(my_dictionary.get("Mindaugas"))

# my_dictionary["Antanas"] = 100

# print(my_dictionary)


# del my_dictionary["Antanas"]

# value = my_dictionary.pop("Antanas")
# print(value)

# print(my_dictionary)

# def my_function():

#     return 2 + 2


# my_val = my_function()

# print(my_val)


# def add_three_numbers(a, b, c):
#     num_sum = a + b + c
#     return num_sum * 52

# add_three_numbers(2, 2, 2)
# print(my_val)

# my_val_sec = add_three_numbers(89, 52, 567)
# print(my_val_sec)

def calc_sum(num_1: float, num_2: int = 10, num_3: int = 20) -> float:
    return num_1 + num_2 + num_3

print(calc_sum(num_1=5.0, num_2=6, num_3=7))