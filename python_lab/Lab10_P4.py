def permute(nums):
    # This function generates permutations using recursion.
    def backtrack(start):
        # If we reached the end of the list, add the current permutation
        if start == len(nums):
            result.append(nums[:])
            return
        
        # Recursively generate all permutations
        for i in range(start, len(nums)):
            # Swap to fix the current position
            nums[start], nums[i] = nums[i], nums[start]
            # Recurse for the rest of the list
            backtrack(start + 1)
            # Backtrack (swap back to undo the current swap)
            nums[start], nums[i] = nums[i], nums[start]
    
    # Sort the list first to ensure permutations are in non-decreasing order
    nums.sort()
    
    result = []
    backtrack(0)
    return result

# Read input
nums = list(map(int, input().split()))

# Generate all permutations
permutations = permute(nums)

# Print each permutation in the required format
for perm in permutations:
    print(" ".join(map(str, perm)))