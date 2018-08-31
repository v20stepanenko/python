# A B C D E F G H

chess_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def is_chess_position(position):
    return (len(position) == 2
            and position[0] in chess_letters
            and position[1].isdigit()
            and int(position[1]) <= 8)

def is_white_place(position):
    if not is_chess_position(position): return
    is_first_white = chess_letters.index(position[0]) % 2 == 0
    is_odd = int(position[1]) % 2 == 0
    if (is_first_white and is_odd) or (not is_first_white and not is_odd) :
        return 'White'
    else:
        return 'Black'


# Start runing proggram
print("Write chess position, please")
chess_position = input().upper()

if is_chess_position(chess_position):
    print(is_white_place(chess_position))
else: print("Your inputed wrong chess position")