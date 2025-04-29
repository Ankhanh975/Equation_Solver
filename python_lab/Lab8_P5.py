# E. Problem 5: Group Anagrams
# You are given a list of words. Two words are called anagrams if one word can be formed by rearranging the letters of another. For example, 'eat' and 'tea' are anagrams of each other.
# Your task is to group all the anagrams together and output the number of anagram groups.

def list_of_revolve(s: str) -> list:
    s = list(s)
    s = sorted(s)
    return s

def check(list_of_revolve: list, test_case: str):
    test_case = list(test_case)
    test_case = sorted(test_case)
    for x in range(len(list_of_revolve)):
        if not list_of_revolve[x] == test_case[x]:
            return False
        
    return True
        
def solve(lines) -> int:
    i = 0
    anagrams = []
    while len(lines) != 0:
        anagram = list_of_revolve(lines[0])
        anagrams.append(lines[0])
        
        # print("anagram", anagram)
        for x in range(len(lines)-1, -1, -1):
            if check(anagram, lines[x]):
                lines.pop(x) 
    
    return len(anagrams)


# Input
# The first line contains an integer n (1≤n≤104), the number of words.
# The following n lines each contain a single word consisting of lowercase English letters.
N = input()
N = int(N)
i = []
for _ in range(N):
    i.append(input())
# N = int(input())
# lines = []
# for x in range(N):
#     s = input()
#     lines.append(s)

# # Output
# # Print only a single number is the number of anagram groups.
print(solve(i))