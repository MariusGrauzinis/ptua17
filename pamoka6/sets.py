my_set = {1, 2, 3}
print(my_set)  # Rezultatas: {1, 2, 3}

# Aibės kūrimas iš sąrašo
my_list = [1, 2, 2, 3, 4]
list_to_set = set(my_list)
print(list_to_set)  # Rezultatas: {1, 2, 3, 4}

for num in my_set:
    print(num)

# Elemento egzistavimo patikrinimas
if 2 in my_set:
    print("2 yra aibėje")