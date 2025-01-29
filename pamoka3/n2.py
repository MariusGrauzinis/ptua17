vardas = input("Įveskite savo vardą:")
pavarde = input("Įveskite savo pavardę:")
amzius = int(input("Įveskite savo amžių:"))

if amzius >= 21:
    print(f"{vardas} {pavarde}, jums leileidžiama patekti į kazino.")
else:
    print (f"{vardas} {pavarde}, jums neleidžiama patekti į kazino.")