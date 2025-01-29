
a, b = 0, 1  
print("Fibonacci seka:", end=" ")

print(a, b, end=" ")

for _ in range(10):  
    
    a, b = b, a + b
    print(b, end=" ")
