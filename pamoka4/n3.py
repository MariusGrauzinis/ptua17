stored_pin = "0022"

for i in range(10000):
    pin = str(i)
    while len(pin) < 4:
        pin = "0" + pin
        print(pin)
    if pin == stored_pin:
        print(f"Surastas PIN: {pin}")
        break