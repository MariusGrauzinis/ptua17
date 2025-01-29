username = "admin"
password = "1234"

while True:
    username = input("Įveskite vartojo vardą: ")
    password = input("Įveskite slaptažodį: ")
    if username == username and password == password:
        print(f"Prisijungimas sėkmingas! Sveiki, {username}.")
        break