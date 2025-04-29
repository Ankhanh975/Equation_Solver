# Problem 3: Custom Alphabet Sorting
# Description:
# Write a Python program that sorts the characters of a given string according to a specified custom
# alphabet order.

def find_min_max(Z: list, custom_order: dict) -> list[int]:
    m1 = float("inf")
    m2 = float("-inf")
    for x in Z:
        m1 = min(m1, custom_order[x])
        m2 = max(m2, custom_order[x])
    return [m1, m2]

def count_frequency(Z: list, m1: int, m2: int, custom_order: dict):
    r = [0] * (m2 - m1 + 1)
    for x in Z:
        r[custom_order[x] - m1] += 1
    return r
def counting_sort(Z: list, custom_order: dict) -> list:
    m1, m2 = find_min_max(Z, custom_order)
    r = []
    frequency = count_frequency(Z, m1, m2, custom_order)
    for i, x in enumerate(frequency):
        for y in range(x):
            r.append(i + m1)
    return r

def build_custom_order_dict(custom: str) -> dict:
    d = dict()
    for i, x in enumerate(custom):
        d[x] = i
    return d
# print(build_custom_order_dict("abcwvutsrqponmlkjihgfedxyz"))

def solve(s: str, custom: str) -> str:
    return_s = ""
    m1, m2 = find_min_max(s, build_custom_order_dict(custom))
    return_s = counting_sort(list(s), build_custom_order_dict(custom))
    return_s = list(map(lambda x: custom[x], return_s))
    return_s2 = ""
    for x in return_s:
        return_s2 += x
    
    return return_s2
# Input:
# The input has two lines:
# • A string composed of lowercase letters that needs to be sorted.
s = input()
# s = "abcwvutsrqponmlkjihgfedxyz"
# • A string representing the custom order of the alphabet.
custom = input()
# custom = "abcwvutsrqponmlkjihgfedxyz"

# Output:
# A string that has been rearranged.
# output = "vvutsrnniiiey"
print(solve(s, custom ))
# Constraints:
# The custom alphabet string contains each letter exactly once.