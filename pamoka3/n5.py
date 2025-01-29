import random

number = random.randint(1, 10)

while True:
    user_guess = int(input("Atspėkite skaičių (1–10): "))
    if user_guess == number:
        print(f"Teisingai! Skaičius yra {number}.")
        break
    elif user_guess < number:
        print("Per mažas! Bandykite dar kartą.")
    else:
        print("Per didelis! Bandykite dar kartą.")