# Write functions that:
# Makes basic math calculations,
# Converts Celsius from faranheit.
# Calculate average speed in meters/sec .Distance is given in Km and time in hours.
# Test all the functions. Prints should be clear and precise.


# Makes basic math calculations,
def calcurator(a, b):
    my_calc1 = a + b
    my_calc2 = a - b
    my_calc3 = a * b
    my_calc4 = a / b  
    
    return my_calc1, my_calc2, my_calc3, my_calc4,

value = calcurator(25, 10)
print(value)





# Converts Celsius from faranheit.
def temperature(a, b, c, d):
    farenheit_temp = (a - b) * c/d
    print(farenheit_temp)
    

temperature ( 80, 32, 5, 9)



    

# Calculate average speed in meters/sec .Distance is given in Km and time in hours.
def average_speed(distance_km, time_hours):
    distance_metr = distance_km * 1000
    time_secund = time_hours * 3600
    average_speed = distance_metr / time_secund
    return average_speed

result = average_speed(1000, 10)
print(result)