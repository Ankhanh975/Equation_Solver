# Write a function enumerate_positive(numbers) that takes a list of numbers and returns a 2D array where each element is an array containing the index and value of a positive number in the list.
def enumerate_positive(numbers: list) -> list:
    array_2d = []
    # Intergrating
    for index, value in enumerate(numbers):
        # If value > 0 and the value to the list with the value index
       if value > 0:
           array_2d.append([index, value])
    
    return array_2d

# Input
# The first line contains an integer n (1≤n≤100), representing the number of elements in the list.


# Get the number of numbers
_ = input()
numbers = list(map(int, input().split()))

# The second line contains n
#  space-separated integers.
# Output
# Output a 2D array where each inner array contains two elements: the index and the positive number from the input list.

print(enumerate_positive(numbers))