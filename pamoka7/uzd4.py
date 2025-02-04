# Makes basic math calculations,
def calculator(num_1: float, num_2: float) -> float:
    calc1 = num_1 + num_2
    calc2 = num_1 - num_2
    calc3 = num_1 * num_2
    calc4 = num_1 / num_2  
    
    return calc1, calc2, calc3, calc4,

value = calculator(num_1 = 25, num_2 = 10)
print(value)





# Converts Celsius from faranheit.
def temperature(celsius: float, farenheit_scale_start: int, scale_cels: int, farenheit_scale: int) ->float:
    farenheit_temp = (celsius - farenheit_scale_start) * scale_cels/farenheit_scale
    return farenheit_temp
    

value = temperature ( celsius = 80, farenheit_scale_start = 32, scale_cels = 5, farenheit_scale = 9)
print(value)



    

# Calculate average speed in meters/sec .Distance is given in Km and time in hours.
def average_speed(distance_km: float, time_hours: int) -> float:
    distance_metr = distance_km * 1000
    time_sec = time_hours * 3600
    average_speed = distance_metr / time_sec
    return average_speed

result = average_speed(distance_km=1000, time_hours=10)
print(result)