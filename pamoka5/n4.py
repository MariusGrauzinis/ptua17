start = int(input("Įveskite intervalo pradžią: "))
end = int(input("Įveskite intervalo pabaigą: "))
primes = []

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
                
        if is_prime:
            primes.append(num)

print("Pirminiai skaičiai:", primes)


