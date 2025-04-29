# A. Problem 1: Counting Word Frequencies

def count_word_frequencies(text: str) -> dict:
    text = text.lower()
    # d is a dictionary
    # A function count_word_frequencies(text) that takes a string text as input and returns a dictionary where the keys are the unique words in the text (case-insensitive), and the values are the number of times each word appears in the text.
    d = {}
    for x in text.split(" "):
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    
    return d

def sort_dict_and_print(d: dict) -> dict:
    # Create a list
    Z = sorted(list(d))
    sorted_d = {}
    for x in Z:
        sorted_d[x] = d[x]
        
    return_s = ""
    for x in sorted_d:
        return_s += f"{x}: {sorted_d[x]}, "
        
    return return_s[:-2]
# Input: The input consists of a single line containing a string text (1≤len(text)≤1000 ). The text contains only lowercase and uppercase letters and spaces. The text will not start or end with a space, and no consecutive spaces will exist.
i = input()
# i = "This is a test this is a test"
# Output
# The output has two lines: the first shows the number of unique words, and the second is a dictionary of word frequencies in alphabetical order, with each key-value pair formatted as "word: frequency" and separated by commas.
# r is return
r = count_word_frequencies(i)
print(len(list(r)))
print(sort_dict_and_print(r))

# Examples
# Input
# This is a test this is a test
# Output
# 4
# a: 2, is: 2, test: 2, this: 2
# Input
# Hello world hello world
# Output
# 2
# hello: 2, world: 2

