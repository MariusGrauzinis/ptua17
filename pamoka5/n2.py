shopping_list = ['pienas', 'kiaušiniai', 'duona', 'sviestas']
print(shopping_list)
print(shopping_list[2])

shopping_list[shopping_list.index("duona")] = "bananas"
print(shopping_list)

shopping_list.insert(0, "obuolys")
print(shopping_list)
more_elements = ['miltai','cukrus']
shopping_list.extend(more_elements)
print(shopping_list)
print(shopping_list[2:4])