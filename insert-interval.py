class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        for i in range(len(intervals)):
            cur_start,cur_end = intervals[i]
            new_start, new_end = newInterval
            if new_end < cur_start:   # the new interval's ed range is before the current interval start, so we can add the new interval and the extend the list to add the remaning intervals
                result.append(newInterval)
                result.extend(intervals[i:])
                return result
            elif new_start > cur_end: # Since the new interval starts after the range of current interval, so we can leave the current interval because the new one does not overlap with it
                result.append(intervals[i])
            else:
                newInterval = [min(new_start, cur_start), max(new_end, cur_end)]  # since the new interval start is in the range of the current interval end, there is a overlap, so we must choose the min for start and max for end of interval 
        # If either of these (new_end < cur_start) or (new_start > cur_end) are not met then the newInternal wouldn't be appended inside the for loop.
        result.append(newInterval)
        return result


Input:  #[[1,3],[6,9]], newInterval = [3,8]
        #[[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [3,10]
        # result = [[1,2],[3,10],[12,16] ]
