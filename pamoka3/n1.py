pirmasskaicius = float(input("Įveskite pirmą skaičių:"))
antrasskaicius = float(input("Įveskite antrą skaičių:"))

if pirmasskaicius > antrasskaicius:
    print("pirmas skaicius didesnis:", pirmasskaicius)
elif pirmasskaicius < antrasskaicius:
    print("antras skaicius didesnis:", antrasskaicius)
else:
    print("Abu skaiciau yra lygus.")