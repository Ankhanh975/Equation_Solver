# A function find_median(numbers) that takes a list of integers as input and returns the median value of the list. The definition of the median can be found in Wikipedia.
def format_number_for_print(number):
    # Format correctly
    return f"{number:.1f}"

def find_median(numbers: list) -> float:
    numbers = sorted(numbers)
    # Get the length of the number list
    length = len(numbers)
    if length % 2 == 1:
        pos = round((length+1)/2)
        element = numbers[pos-1]
    else:
        pos1 = round(length/2)
        pos2 = round(length/2+1)
        element1 = numbers[pos1-1] 
        element2 = numbers[pos2-1] 
        element = (element1 + element2) / 2
    return element

# Input
# The first line contains an integer n (1≤n≤100), representing the number of elements in the list.
# The second line contains n space-separated integers (each integer is between -1000 and 1000).

# Get the number of numbers
_ = input()
numbers = list(map(int, input().split()))
# Output
# Output the median of the list. If the median is an integer, output the integer. If the median is a float, output the float with one decimal place.
print(find_median(numbers))