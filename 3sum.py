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
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Input: [-2,0,0,2,2], Output: [[-2,0,2],[-2,0,2]] - Duplicate triplicate scenario
        #Input: [-1,0,1,2,-1,-4], Output: [[-1,-1,2],[-1,0,1],[-1,0,1]] - Duplicate triplicate scenario
        res = []
        nums.sort()
        for i in range(len(nums)): #len(nums)=5
            #If the current value is greater than zero, break from the loop. Remaining values cannot sum to zero.
            if nums[i] > 0:
                break
             # To avoid duplicate triplicates from being formed in the list the below if condition needed
    
            if i == 0 or nums[i - 1] != nums[i]:
               self.twoSumII(nums, i, res)
        return res
        
    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
