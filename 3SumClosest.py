from typing import List

class Solution:

        def threeSumClosest(self, nums: List[int], target: int) -> int:
            """
            Finds the three integers in 'nums' that sum closest to 'target'.
            """
            # Initialize a variable to track the smallest difference found so far:
            diff = float('inf')  # Start with an infinitely large difference
            # Sort the list to enable efficient two-pointer search:
            nums.sort()
            # Iterate through each element as the potential first number in a triplet:
            for index, element in enumerate(nums):
                # Initialize two pointers to explore the remaining subarray:
                lo, hi = index + 1, len(nums) - 1
                # Two-pointer approach to find potential triplets:
                while lo < hi:
                    # Calculate the current sum using the three pointers:
                    sum = element + nums[lo] + nums[hi]
                    # Check if the current sum is closer to the target than any previous sum:
                    if abs(target - sum) < abs(diff):
                        diff = target - sum  # Update the smallest difference
                    # Move pointers towards a closer sum:
                    if sum < target:
                        lo += 1  # Increase the sum by moving the left pointer
                    else:
                        hi -= 1  # Decrease the sum by moving the right pointer
                    # Terminate early if an exact match is found:
                    if diff == 0:
                        break        
            # Return the target value minus the smallest difference, which is the closest sum:
            return target - diff

  
def threeSumClosest(self, nums: List[int], target: int) -> int:
    """
    Finds the three integers in 'nums' that sum closest to 'target'.

    Args:
        nums: A list of integers.
        target: The target sum.

    Returns:
        The sum of the three integers closest to 'target'.
    """

    # Handle invalid input:
    if not nums or len(nums) < 3:
        return 0  # Insufficient elements for a triplet

    # Sort the list for efficient searching using two pointers:
    nums.sort()

    # Initialize a variable to track the closest sum found so far:
    closest_sum = float('inf')

    # Iterate through each element as the potential first number in a triplet:
    for i in range(len(nums) - 2):

        # Skip duplicates for the first number to avoid redundant calculations:
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Initialize two pointers to explore the remaining subarray:
        left, right = i + 1, len(nums) - 1

        # Two-pointer approach to find potential triplets:
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            # Check if an exact match is found:
            if current_sum == target:
                return current_sum  # Perfect match, return immediately

            # Update the closest sum if the current sum is closer to the target:
            if abs(target - current_sum) < abs(closest_sum - target):
                closest_sum = current_sum

            # Move pointers based on the comparison with the target:
            if current_sum < target:
                left += 1  # Increase the sum by moving the left pointer
            else:
                right -= 1  # Decrease the sum by moving the right pointer

    # Return the closest sum found after exploring all possible triplets:
    return closest_sum


# Optimizations and considerations:
# Early Exit: The condition if current_sum == target is added to break out of the loop early if the exact target sum is found, reducing unnecessary iterations.
# Remove Redundant Break: The if diff == 0 condition is not needed in this case because the loop already breaks when the exact target sum is found.
# Variable Name: Changed the variable name from sum to current_sum to avoid shadowing the built-in sum function.
# This code maintains the efficiency of the original solution while providing some clarity and handling edge cases. Note that the time complexity remains O(n^2), where "n" is the length of the input array nums.

# Example usage:
nums = [-1, 2, 1, -4]
target = 1
solution = Solution()
result = solution.threeSumClosest(nums, target)
print(result)
