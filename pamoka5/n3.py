size = int(input("Įveskite trikampio dydį: "))

for i in range(1, size + 1):
    for a in range(1, i + 1):
        print(a, end=" ")
    print()