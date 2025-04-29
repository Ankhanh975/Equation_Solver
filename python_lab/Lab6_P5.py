# E. Problem 5: Analyzing Character Frequencies in Words
# Write a function analyze_words(words) that takes a list of words as input and returns a list of strings that describes the frequency of each character in each word, in the format "character: count". Each string in the output list should correspond to a word in the input list and be constructed using list comprehension. The output should also include the word index in the input list. The character counts should be printed in alphabetical order.

def analyze_word(word: str) -> str:
    # Get unique charecters of the word using set() property
    set_intant = set()
    for char in word:
        set_intant.add(char)
    
    # Use dictonary to count
    unique_chars = {}
    for char_to_check in set_intant:
        unique_chars[char_to_check] = 0
    
    # Count each into its bin
    for char in word:
        unique_chars[char] += 1
    
    #Order it alphabatically
    sorted_unique_chars = {key: value for key, value in sorted(unique_chars.items())}
    
    # Now we convert the list into string
    s= ""
    for key in sorted_unique_chars:
        s += f"{key}: {sorted_unique_chars[key]}, "
    
    # Cut the last two chars
    s = s[:-2]
    return s

def analyze_words(words: list[str]) -> str:
    return_string = ""
    # Do counting unique chars for each word 
    for index, word in enumerate(words):
        return_string += f"{index} - {analyze_word(word)}" + "\n"
        
    return_string = return_string[:-1]
    return return_string      

# For each word, list each unique character and its frequency.
# The output for each word should be formatted as "word_index — character1: count1, character2: count2, ...".
# Input
# The first line contains an integer n (1≤n≤100), representing the number of words.
# Get the number of numbers
_ = input()
# The second line contains n space-separated strings.
words = list(map(str, input().split(" ")))

# Output
# Output a list of strings, each representing the character frequencies for the corresponding word, sorted alphabetically by character.
print(analyze_words(words))
