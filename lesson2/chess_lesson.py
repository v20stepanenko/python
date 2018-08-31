# Написать 5 програм, для каждой фигуры: ферзь, король, слон, ладья, конь.
#  Програмы определяют допустимость хода шахматной фигурой от координат до координат, которые пользователь вводит
#  в виде шахматной нотации через -: c3-a1, b2-b4

import re

chess_letters = {'A' : 1, 'B' : 2,
                 'C' : 3, 'D' : 4,
                 'E' : 5, 'F' : 6,
                 'G' : 7, 'H' : 8}

input_moving = input().upper()
check_moving = re.match(r'^([A-H][1-8])[-_\s]{0,3}([A-H][1-8])$', input_moving)

def position_num(position):
    return([int(chess_letters[position[0]]), 
        int(position[1])])

def get_pos_indexes(cur, new):
    return (abs(current_position[0] - new_position[0]),
            abs(current_position[1] - new_position[1]))

def moving_knight(indexes):
    is_magic_num_kinght = (indexes[0] + indexes[1]) == 3
    if(indexes[0] != 0 and indexes[1] != 0 and is_magic_num_kinght):
        return 'Yes'
    else:
        return 'No'

def moving_king(indexes):
    if(indexes[0] <= 1 and indexes[1]):
        return 'Yes'
    else:
        return 'No'

def moving_bishop(indexes):
    if(indexes[0] == indexes[1]):
        return 'Yes'
    else:
        return 'No'

def moving_castle(indexes):
    if(indexes[0] == 0 or indexes[1] == 0):
        return 'Yes'
    else:
        return 'No'

def moving_queen(indexes):
    if( (indexes[0] == 0 or indexes[1] == 0) 
        or (indexes[0] == indexes[1]) ):
        return 'Yes'
    else:
        return 'No'

if(check_moving):
    current_position = position_num(input_moving[:2])
    new_position = position_num(input_moving[-2:])
    direction_indexes = get_pos_indexes(current_position, new_position)
    print(moving_queen(direction_indexes))
else:
    print('You wrote wrong chess step')