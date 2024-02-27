class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')# 
        nums.sort() # required to use the 2-pointer approach efficiently.
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while (left < right): # this work because array is sorted. This loop will help find the other 2 elements in the triplet.
                # calculate the current sume of 3 variables.
                sum = nums[i] + nums[left] + nums[right]
                # find the absolute difference bw target and sum
                # compare the absolute difference with the current diff. 
                # If the absolute diff is smaller we would update the absolute diff to the smaller value. This steps is crucial as we are interested in finding closest sum to the target.
                # In this way we would guarantee the diff is going to be smaller,smaller and smaller by each iteration
                if abs(target - sum) < abs(diff): 
                    diff = target - sum
                if sum < target:             
                    left += 1 # if you want to have an higher sum, the low pointer needs to be pushed up. This guarantees an higher sum. Moving towards larger value.
                else:
                    # if we want to decrease our sum, we will push the right pointer down. Moving towards smaller value.
                    right -= 1
            # if diff == 0: # Not needed works without this 
            #     break
        return target - diff

#nums = [-1,2,1,-4], target = 1
