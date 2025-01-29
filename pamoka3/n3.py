pirmasskaicius = int(input("Įveskite pirmą skaičių:"))
simbolis = input("Įveskite simbolį (+, -, *, /):")
antrasskaicius = int(input("Įveskite antrą skaičių:"))

atsakymas = None


if simbolis == "-":
    atsakymas = pirmasskaicius - antrasskaicius
elif simbolis == "+":
    atsakymas = pirmasskaicius + antrasskaicius
elif simbolis ==  "/":
    atsakymas = pirmasskaicius / antrasskaicius
elif simbolis == "*":
    atsakymas = pirmasskaicius * antrasskaicius
else:
    atsakymas = "Negalimas"
print(f"{pirmasskaicius} {simbolis} {antrasskaicius} atsakymas yra {atsakymas}")

