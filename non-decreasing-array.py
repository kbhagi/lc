class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
         # there are 2 parts to this problem. 
         # Part 1: finding the violation count. if > 1 return False. keeping a track of the count of violation such that by just modifying a single element we need to be able to make the array non decreasing. This is to meet the problem constraint.
         #Ex: [3,4,2] --> [3,2,2] or [3,4,4] 
         # Part 2: fixing the violation ensuring that another violation does not occur. nested if condn inside the outer if because just by doing nums[i-1]=nums[i] may lead to another violation i.e still array being decreasing. To avoid this, we make an additional check for nums[i-2] > nums[i] thereby assing nums[i]=nums[i-1]
         violation_count=0
         for i in range(1,len(nums)):
             if nums[i] < nums[i-1]:
                if violation_count==1:
                   return False
                violation_count+=1
                if i>=2 and nums[i-2] > nums[i]:
                    nums[i] = nums[i-1]
         return True
