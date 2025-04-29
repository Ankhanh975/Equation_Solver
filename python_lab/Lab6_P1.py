# Sum all the elements in the list.
# Find the minimum value in the list.
# Find the maximum value in the list.
# Reverse the list.
# Each of these operations should be outputted on a separate line in the following order:


# function list_operations(numbers) that takes a list of numbers as input and performs the following operations
def list_operations(numbers: list) -> tuple:
    # The sum of the elements.
    # The minimum element.
    # The maximum element.
    # The reversed list as space-separated values.
    # Input
    # The first line contains an integer n
    #  (1≤n≤100
    # ), representing the number of elements in the list.
    # The second line contains n
    #  space-separated integers (each integer is between −1000
    #  and 1000
    # ).
    
    # Sum all the elements in the list.
    s = 0
    for i in numbers:
        s += i
        
    # Find the minimum value in the list.
    min = numbers[0]
    for i in numbers:
        if i < min:
            min = i
            
    # Find the maximum value in the list.
    max = numbers[0]
    for i in numbers:
        if i > max:
            max = i
            
    # Reverse the list.
    Z = []
    for i in range(0, len(numbers)):
        Z.append(numbers[-1-i])
    return s, min, max, Z



# Using numbers = list(map(int, input().split())) reads the input list of integers. It reads the input line, splits it into a list of strings, and then converts each string to an integer.
# Get the number of numbers
_ = input()
numbers = list(map(int, input().split()))

answer = list_operations(numbers)
total = answer[0]
min = answer[1]
max = answer[2]
reverse_list = answer[3]

# Output
# The output should contain the results of the four operations, each on a separate line.
# The * operator is used to unpack the list when printing the reversed list. If you print a list directly, it will be enclosed in square brackets.

print(total)
print(min)
print(max)
print(*reverse_list)

