# D. Problem 4: Filtering Words by Length Using List Comprehension
# A function filter_by_length(words, min_length) that takes a list of words and returns a new list of words that are at least min_length characters long.

def filter_by_length(words, min_length: int):
    suitable_string = []
    for each_string in words:
        if len(each_string) >= min_length:
            suitable_string.append(each_string)
    return suitable_string
# Input
# The first line contains an integer n (1≤n≤100), representing the number of strings.
# Get the number of numbers
_ = input()

# The second line contains n space-separated strings.
words = list(map(str, input().split()))

# The third line contains an integer representing the minimum length.
minimum_length = int(input())
# Output
# Output a space-separated list of words that meet the length condition.

print(*filter_by_length(words, minimum_length))