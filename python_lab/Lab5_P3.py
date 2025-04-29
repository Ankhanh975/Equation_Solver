

def from_coords_to_str_encoder(x: int, y: int) -> bool:
    return f"{chr(x+97)}{y+1}"

def all_valid_posistion_to_move(pos: str) -> list:
    # row run from 0 to 7, collum runs from 0 to 7
    row = int(ord(pos[0])) - 97
    collum = int(pos[1]) - 1
    # A list of total possible moves
    Z = []
    if 0 <= row + 1 < 8 and 0 <= collum + 1 < 8 :
        Z.append(from_coords_to_str_encoder(row + 1, collum +1))
    if 0 <= row < 8 and 0 <= collum + 1 < 8 :
        Z.append(from_coords_to_str_encoder(row, collum +1))
    if 0 <= row - 1 < 8 and 0 <= collum + 1 < 8 :
        Z.append(from_coords_to_str_encoder(row - 1, collum +1))
        
    if 0 <= row + 1 < 8 and 0 <= collum  < 8 :
        Z.append(from_coords_to_str_encoder(row + 1, collum))
    if 0 <= row - 1 < 8 and 0 <= collum  < 8 :
        Z.append(from_coords_to_str_encoder(row - 1, collum))
        
    if 0 <= row + 1 < 8 and 0 <= collum - 1 < 8 :
        Z.append(from_coords_to_str_encoder(row + 1, collum - 1))
    if 0 <= row < 8 and 0 <= collum - 1 < 8 :
        Z.append(from_coords_to_str_encoder(row, collum - 1))
    if 0 <= row - 1 < 8 and 0 <= collum - 1 < 8 :
        Z.append(from_coords_to_str_encoder(row - 1, collum - 1))
    
    return Z

def check(first_line:str, second_line: str) -> bool:
    Z = all_valid_posistion_to_move(first_line)
    for x in Z:
        if second_line == x:
            return True
    # Otherwise, return False
    return False
    
# a Python program that verifies whether a move made by the King in a chess game is legal according to the rules of chess. Rules for King's Movement:
# The King can move exactly one square horizontally, vertically, or diagonally. This means the King can move to any of the eight surrounding squares from a given position.
# Input
# The input consists of two lines. Each line has two characters.
first_line = input()
second_line = input()
# Output
# A boolean value presents whether the given move is valid or not.
print(check(first_line, second_line))