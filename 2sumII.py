from typing import List

# two-pointer approach
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    # [2,7,11,15], target=9
    # [2,3,4], target = 6
    # [-1,0], target = -1
    left, right = 0, len(numbers) - 1
    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left + 1, right + 1]
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            right -= 1

# hash-table
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    map = {}
    for i in range(len(numbers)):
        complement = target - numbers[i]
        if complement not in map:
            map[numbers[i]] = i
        else:
            return [map[complement] + 1, i + 1]


# binary search
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    for i in range(len(numbers)):
        left, right = i + 1, len(numbers) - 1
        complement = target - numbers[i]
        while left <= right:
            mid = left + (right - left) // 2
            if numbers[mid] == complement:
                return [i + 1, mid + 1]
            elif numbers[mid] < complement:
                left = mid + 1
            else:
                right = mid - 1
