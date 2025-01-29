 my_list = [1, 2, 3, 4, 5]

a = 2

my_dictionary = {"Antanas": 1, "Jonas": 2, "Petras": 3}

print(my_dictionary)

print(my_dictionary["Mindaugas"])

print(my_dictionary.get("Mindaugas"))

my_dictionary["Antanas"] = 100

print(my_dictionary)


del my_dictionary["Antanas"]
value = my_dictionary.pop("Antanas")
print(value)

print(my_dictionary)