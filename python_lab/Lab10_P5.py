# Problem 5: Permutation Generation
# Description:
# You are given a list of distinct integers, and your task is to generate all possible permutations of the elements
# in the list. The generated permutations must be sorted in non-decreasing order.
def permutations(Z: list) -> list:
    # print("Called to permutations_2()", Z)
    
    if len(Z) == 1:
        return [Z]
    else:
        previous_work = permutations(Z[:-1])
        this_loop_work = Z[-1]
        new_Z = []
        temp = len(previous_work)
        temp2 = len(previous_work[0])
        for i2 in range(temp):
            for i1 in range(temp2):
                # print("i2", i2, i1, previous_work[i2][:i1], [this_loop_work], previous_work[i2][i1:])
                new_Z.append(previous_work[i2][:i1] + [this_loop_work] + previous_work[i2][i1:])
            new_Z.append(previous_work[i2] + [this_loop_work])
        
        return new_Z
    
def format_print_final(Z: list) -> str:
    Z = sorted(Z)
    s = ""
    for x in Z:
        for y in x:
            s += str(y) + " "
        s += "\n"
    return s
 
# print(permutations([0, 1, 2, 3]))
# 
 
# Input:
# The program takes a list of distinct integer numbers as input. The list ‘nums‘ contains at most 8 distinct
# integers, and each integer is unique within the list.
i = input()
i = i.split()
i = list(map(int, i))
# Output:
# Return a list of lists representing all possible permutations of the elements in the input list. The list must be
# sorted in non-decreasing order.
# print(permutations([2, 5, 3]))
print(format_print_final(permutations(i)))