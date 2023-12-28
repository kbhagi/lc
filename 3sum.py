class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums)):
            # Avoid duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Two pointers approach
            left = i + 1
            right = len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum > 0:
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    # Move pointers to avoid duplicates
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    

        return results 
