def count_vowels(text: str) -> int:
    # input: text representing a string, containing n number of vowels chars
    # output: integer representing the number of vowels in the string
    
    count = 0
    for char in text:
        if char in "aeiouAEIOU":
            count += 1
            
    return count;

# Test code
if __name__ == "__main__":
    text = input("")
    print(count_vowels(text))