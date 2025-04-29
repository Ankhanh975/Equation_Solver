# Lab 07: Lists, iteration, and loops
# Problem 2: Finding the Smallest Missing Positive Integer
# Description: Given a list of integers, determine the smallest positive integer that is not present in the list. A python program to solve this problem in two different ways: for loop and while loop.

# Input: Player list: A list of positive integers, separated by space, having length from 1 to 100. Each positive integer has ranges from −105 to 105

# Read in the list Z
Z = map(int, input().split(" "))
Z = list(Z)

# Part (a): 
def smallest_integer_for(Z: list) -> int:
    # Using a for loop
    # A function smallest integer for that takes the given list as input and returns the smallest missing positive integer. This function use the for loop to solve the problem.
   
    def get_smallest_posistive_number(Z: list):
        s = Z[0]
        for x in Z:
            if x < s:
                s = x
        if s <= 0:
            s = 1
        return s
    
    def get_largest_number(Z: list):
        s = Z[0]
        for x in Z:
            if x > s:
                s = x
        return s
    
    for x in range(1, get_largest_number(Z) + 2, 1):
        if x not in Z:
            return x
    
    return 1

# Part (b): Using a while loop
def smallest_integer_while(Z: list) -> int:
    # A function smallest integer while that takes the given list as input and returns the smallest missing positive integer. This function must use the while loop to solve the problem.
    # This way shows while loop’s strengths in handling conditions that are not tied to the length of the list.
    def is_Valid(smallest_interger: int, Z: list):
        isValid = True
        for x in Z:
            if x == smallest_interger:
                isValid = False
        return isValid
    
    smallest_integer_yet = 1
    while not is_Valid(smallest_integer_yet, Z):
        smallest_integer_yet += 1
    
    return smallest_integer_yet

# Output:
# Output the smallest positive integer missing from the list using two lines: the first line employs a for loop, while the second utilizes a while loop.
print(smallest_integer_for(Z))
print(smallest_integer_while(Z))
