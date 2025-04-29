# Lab 07: Lists, iteration, and loops
# Problem 3: Count the Valleys

# Example:
# Given the path DDUUDDUDUUUD.
# • The path starts at sea level.
# • The first DD means the path goes down two steps below sea level, starting a valley.
# • The subsequent UU brings the hiker back to sea level, thus completing one valley.
# • The next DD starts another descent but the following U brings it up only one step, so it’s not yet
# back to sea level.
# • Another D takes the hiker further down again.
# • The final UUUD brings the path up to sea level and then above, completing the second valley during
# the UU part.

def solve(s: str) -> int:
    # Description: You are given a string where each character signifies either a step up (U) or a step down (D) from a flat baseline known as sea level. The task is to count the number of distinct valleys formed during the path, where a valley is a sequence of steps starting with a step down from sea level and ends when you step back up to sea level.
        
    level = 0
    valleys = 0
    in_valley = False

    for step in s:
        if step == 'U':
            level += 1
        elif step == 'D':
            level -= 1

        if level < 0 and not in_valley:
            in_valley = True
        if level == 0 and in_valley:
            valleys += 1
            in_valley = False

    return valleys
        

# Input: The input has a single string where each character represents a step and can be either U (up) or D (down). This string’s length ranges from 3 to 104.

s = input()
# s = "UDDDUUUUUUDDDUDDD"

# Output: An integer representing the number of valleys traversed in the given string.
print(solve(s))


