# Problem 2: Merge sort
# Description:
# Given an unsorted list of integers, implement the Merge Sort algorithm to sort the list in ascending order.
# Your task is to complete the following sub-problems:
# Part (a): Initialize Chunks
# Objective: Prepare the list for the sorting process by splitting it into the smallest possible sorted lists.
# Task: Write a function named initialize chunks that takes the integer list as the input and returns
# the list of single-element lists. For example, given the input [1, 9, 3, -1], the function will return
# [[1], [9], [3], [-1]].
def initialize_chunks(Z: list):
    Z = map(lambda x: [x], Z)
    Z = list(Z)
    return Z

# print(initialize_chunks([1, 2, 3, 2, 1]))
# Part (b): Merge two lists
# Objective: Compare the elements of two sorted lists sequentially, appending the smaller element to a
# new list, thus maintaining order. Continue this process until all elements from both lists are included in
# the new, merged list.
# Task: Write a function named merge two list that takes the two ascendingly sorted lists as the input
# and returns a single sorted list in ascending order. For example, given two sorted lists [27, 38] and [3,
# 43], the function will return [3, 27, 38, 43].

def merge_two_list(list_a: list, list_b: list) -> list:
    list_c = []
    pointer_a = 0
    pointer_b = 0
    while len(list_c) < len(list_a) + len(list_b):
        # print(list_c, pointer_a, pointer_b)
        
        if pointer_a <= len(list_a) - 1 and pointer_b <= len(list_b) - 1 and list_a[pointer_a] < list_b[pointer_b]:
            list_c.append(list_a[pointer_a])
            pointer_a += 1
        elif pointer_a <= len(list_a) - 1 and pointer_b <= len(list_b) - 1:
            list_c.append(list_b[pointer_b]) 
            pointer_b += 1
        else:
            if pointer_a <= len(list_a) - 1:
                list_c.append(list_a[pointer_a])
                pointer_a += 1
            else:
                list_c.append(list_b[pointer_b])
                pointer_b += 1
    return list_c

# print(merge_two_list([27, 38, 100], [3, 43]))
# print("done")

# Part (c): Merge Sort
# Objective: Apply the merge function iteratively to all pairs of adjacent sub-lists. With each iteration,
# the size of the sorted sub-lists doubles.
# Task: Write a function named merge sort that takes an unordered list as the input and returns the
# sorted list in ascending order. The function needs to apply the above-built functions in Parts (a) and
# (b). For example, given the unordered lists [1, 9, 3, -1], the function will return [-1, 1, 3, 9].
# Input:
def merge_sort(Z: list[list]) -> list:
    Z = initialize_chunks(Z)

    while len(Z) != 1:
        new_Z = []
        for x in range(0, len(Z), 2):
            # print(Z[2*x], Z[2*x+1], merge_two_list(Z[2*x], Z[2*x+1]))
            if x < len(Z) - 1 :
                new_Z.append(merge_two_list(Z[x], Z[x + 1]))
            else:
                new_Z.append(Z[x])
                
        Z = new_Z
    return new_Z


# A list of integers, separated by space, each number ranges from −100 to 100. The amount of integers
# ranges from 2 to 100.
# i = input()
i = "4 3 2 5 3 4 1 -1"
i = i.split()
i = map(int, i)
i = list(i)
# print(i)

# Output:
# The outputs should consist of the following lines:
# • The first line describes the list of single-element lists.
print(initialize_chunks(i))
# • The second line shows the list from combining two adjacent single-element lists from the first line.
Z = initialize_chunks(i)
new_Z = []
for x in range(0, len(Z), 2):
    if x < len(Z) - 1 :
        new_Z.append(merge_two_list(Z[x], Z[x + 1]))
    else:
        new_Z.append(Z[x])
print(new_Z)
# • The third line returns the fully sorted list.
print(merge_sort(i)[0])
# Requirements:
# The students are not allowed to use any built-in sorting functions or methods.



import time
i = "4 3 2 5 3 4 1 -1"
i = i.split()
i = map(int, i) 
i = list(i)
n = i
start_time = time . perf_counter ()
merge_sort(i)
end_time = time . perf_counter ()
print(end_time - start_time)



# Comments these results at the end of the program

"""
 Input : 4 3 2 5 3 4 1 -1
 Execution Time : 2.089992631226778e-05 seconds

 Input : 4 3 2 5 3 4 1 -1 4 3 2 5 3 4 1 -1 4 3 2 5 3 4 1 -1 4 3 2 5 3 4 1 -1
 Execution Time : 5.01e-05 seconds
"""
