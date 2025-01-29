unique_numbers = []

while True:
    entry = input("Įveskite sveikąjį skaičių (arba 'pabaiga'): ")
    if entry == "pabaiga":
        break
    number = int(entry)
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)
