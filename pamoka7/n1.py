def calculate_kmi(weight, height):
    kmi = weight / (height ** 2)  
    return kmi 

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

kmi = calculate_kmi(weight, height)
print(f"Your KMI: {kmi}.")