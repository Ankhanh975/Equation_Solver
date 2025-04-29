# Lab 07: Lists, iteration, and loops
# Problem 4: Student Ranking

# Description: 
#  A system to dynamically manage and sort a list of players based on their scores for a tournament. The system must efficiently handle adding new players, removing players, and adjusting existing scores while keeping the list organized by descending score. If scores are tied, players should be sorted alphabetically by name. Your challenge is to write a Python program that implements this dynamic player management system.

# We have 3 specific operations in this system:
# 1. Insert a Player: Add a new player along with their score to the system. The operation is formatted as insert PlayerName Score within the operations string.
# 2. Remove a Player: Remove a player from the system by their name. The operation is formatted as remove PlayerName within the operations string.
# 3. Adjust a Player’s Score: Modify the score of an existing player, either increasing or decreasing it. The operation is formatted as adjust PlayerName ScoreChange within the operations string.

# Input:
# Player list: The first line contains a single string including players and their scores in the format
# PlayerName Score, separated by commas.
# Operation list: The second line contains a single string including operations, where each operation is represented in the format operation operation PlayerName [Score or Nothing], separated by commas.

i = input()
# Extra instructions for the database problem 
second_line = input()

# i = "Phuc 1500, Vinh 1500, Mien 1500"
# second_line = "insert Thinh 1400, adjust Phuc -100, adjust Vinh -100, adjust Mien -100"
i = i.split(", ")


# Part (a): Convert Input into Nested List
# Write a function convert input to convert the initial input into a nested list, where each component of the list is a two-element list containing the player’s name and score with format [Player, Score].

def sub_split(s: str):
    return s.split(" ", 1)
i = list(map(sub_split, i))

# Part (b): Perform Operations
# Write a function perform operation to execute the operations on the player list: adding new players, removing players, and adjusting scores. This function returns the final list after completing all operations.

# Serparate out single cmds
# Example input: Thinh 1400, "adjust" Phuc -100, "adjust" Vinh -100, "adjust" Mien -100
second_line = second_line.split(", ")
second_line = list(map(sub_split, second_line))

def remove_by_name(s: list, name: str) -> None:
    for x in range(len(s)):
        if s[x][0] == name:
            s.pop(x)
            return
        
def adjust_by_value(s: list, name: str, new_score: int) -> None:
    for x in range(len(s)):
        if s[x][0] == name:
            s[x][1] = int (s[x][1])     + int (new_score)
            return

for instruction, parameters in second_line:
    if instruction == "insert":
        name, score = parameters.split(" ")
        i.append([name, score])
    elif instruction == "adjust":
        name, score = parameters.split(" ")
        adjust_by_value(i, name, score)
    elif instruction == "remove":
        remove_by_name(i, parameters)


# Part (c): Sort the List
# Write a function sort player that takes the final list as input and sort it by score in descending order. If two players have the same score, sort them alphabetically by their names.
# Output: Print the list of players (name only) sorted from highest to lowest score. For players with the same score, print them in alphabetical order by name.

def sorting_citiria(value):
    return (-int(value[1])), value[0]

i.sort(key = sorting_citiria)
i = map(lambda x: x[0], i)
i = list(i)
s = ""
for x in i:
    s += str(x) + " "

print(s)
    