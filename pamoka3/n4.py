narys = input("Ar esate bibliotekos narys? (taip / ne):")



if  narys == "taip":
    amzius = int(input("Įveskite savo amžių:"))
    if amzius >= 12:
              print ("Jūs galite skolintis visas knygas.")
    else:
         suaugęsasmuo = input("Ar jus lydi suaugęs asmuo? (taip / ne):")
         if  suaugęsasmuo == "taip":
              print("Jūs galite skolintis visas knygas.")
         else:
              print("Jūs galite skolintis tik vaikų knygas.")
else:
    print("Jūs negalite skolintis jokių knygų.")



