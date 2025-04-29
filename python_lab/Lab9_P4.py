# Problem 4: k-th Largest Element
# Description:
# Write a Python program that uses binary search to find the k-th largest element in a given unsorted list,
# where each number within the list is unique.

def sort(array):
    """Sort the array by using quicksort."""

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array
    
# Input:
# The input has two lines:
# • A list of integers, separated by space. Each integer ranges from −100 to 100. The list’s length n
# ranges from 2 to 100.
i = input()
# i = "100 -100 6 7 -7 -6 2"
i = i.split()
i = map(int, i) 
i = list(i)

# • An integer k displaying the expected k-th largest element in a given unsorted list, ranging from 0
# to n − 1.
k = int(input())
# k = 3
i = sort(i)

# Output:
# The k-th largest element in the given unsorted list.
print(i[len(i) - k])
# Example:
# Test case 1
# Input:
# 3 2 1 5 6 4
# 2
# Output:
# 5
# Test case 2
# Input:
# 100 -100 6 7 -7 -6 2
# 3
# Output:
# 6
