# Write a Python program that takes a string as input and encodes it following these rules in sequence, ensuring each rule is case-sensitive:
# - If the string contains the word secret, replace it with XXXXXX.
# - Replace all occurrences of a, e, i, o, u with @, 3, !, 0, v, respectively.

s = input()
s = s.replace("secret", "XXXXXX")
new_s = ""
for x in s:
    if x == "a":
        x = "@"
    if x == "e":
        x = "3"
    if x == "i":
        x = "!"
    if x == "o":
        x = "0"
    if x == "u":
        x = "v"
        
    new_s += x

# Input
# The input has one line consisting of one string, having length from 1
#  to 109
# .

# - Convert characters to uppercase if the string length is even, and to lowercase if it is odd, after applying the previous rules.
if len(new_s) % 2 == 0:
    new_s = new_s.upper()
elif len(new_s) % 2 == 1:
    new_s = new_s.lower()
     

# Output
# One string represents the encoded text.
print(new_s)
