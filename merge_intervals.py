class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        for i in range(len(intervals)):  #Time Complexity O(n) + O(n log(n)) = O(n)
            if merged == []:             #Space Complexity O(n)
                merged.append(intervals[i])
            else:
                previous_end = merged[-1][1]
                current_start = intervals[i][0]
                current_end = intervals[i][1]
                if previous_end >= current_start: # overlap
                    merged[-1][1] = max(previous_end,current_end)
                else:
                    merged.append(intervals[i])
        return merged

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key=lambda x: x[0])
        for i in intervals:
            # if the list of merged intervals is empty 
      			# or if the current interval does not overlap with the previous,
      			# simply append it.
            if not merged or merged[-1][-1] <= i[0]:
                merged.append(i)
      			# otherwise, there is overlap,
      			#so we merge the current and previous intervals.
            else:
                merged[-1][-1] = max(merged[-1][-1], i[-1])
        return merged
