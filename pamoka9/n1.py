def puzzle_pieces(*args):
    # Patikriname, ar visi sąrašai turi tą pačią ilgį
    length = len(args[0])
    for lst in args:
        if len(lst) != length:
            return False
    
    # Naudojame lambda funkciją, kad apskaičiuotume sumą
    sum_check = lambda x, y: x + y
    
    # Patikriname, ar kiekvienos atitinkamų elementų sumos yra vienodos
    for i in range(length):
        sum_value = sum_check(args[0][i], args[1][i])  # Pirmųjų dviejų sąrašų elementų suma
        for lst in args[2:]:
            if sum_check(lst[i], args[0][i]) != sum_value:
                return False

    return True

print(puzzle_pieces([1, 2, 3, 4], [4, 3, 2, 1]))  # True
print(puzzle_pieces([1, 8, 5, 0, -1, 7], [0, -7, -4, 1, 2, -6]))  # True
print(puzzle_pieces([1, 2], [-1, -1])) 
print(puzzle_pieces([9, 8, 7], [7, 8, 9, 10]))