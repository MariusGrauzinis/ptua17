def puzzle_pieces(*args):
    length = len(args[0])
    for lst in args:
        if len(lst) != length:
            return False
    
  
print(puzzle_pieces([1, 2, 3, 4], [4, 3, 2, 1]))
print(puzzle_pieces([1, 8, 5, 0, -1, 7], [0, -7, -4, 1, 2, -6]))
print(puzzle_pieces([1, 2], [-1, -1])) 
print(puzzle_pieces([9, 8, 7], [7, 8, 9, 10]))