""" The problem presents a scenario where we have an array of meeting time intervals, each represented by a pair of numbers [start_i, end_i]. These pairs indicate when a meeting starts and ends. The goal is to find the minimum number of conference rooms required to accommodate all these meetings without any overlap. In other words, we want to allocate space such that no two meetings occur in the same room simultaneously."""

    
#intervals = [[0,30],[5,10],[15,20]], output =2
# intervals = [[7,10],[2,4]], output = 1
   
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = [] # Define 2 arrays starts and ends to store the each start and end time's separately.
        ends = []
        rooms, ends_idx = 0,0  # rooms is the variable that would be returned
        for i in intervals:  # Store stars, ends separately
            starts.append(intervals[i][0])
            ends.append(intervals[i][-1])
        starts.sort() #
        ends.sort()
        for i in starts:
            # Start is smaller than end, add one room
            #if the start interval is less than the end interval increment the room counter since we would need a extra room, else decrement the count since we have freed up the room.
            if starts[i] < ends[ends_idx]:
                rooms+=1
            else: #  if starts[i] < ends[ends_idx], we cannot use a room we used before, otherwise we can reuse a room.
                ends_idx+=1
        return rooms


"""
The numbers of the intervals give chronological orders
When an ending event occurs, there must be a starting event has happened before that, where “happen before” is defined by the chronological orders given by the intervals
Meetings that started which haven’t ended yet have to be put into different meeting rooms, and the number of rooms needed is the number of such meetings.Initially, endsItr points to the first end event, and we move i which is the start event pointer. As we examine the start events, we’ll find the first two start events happen before the end event that endsItr points to, so we need two rooms (we magically created two rooms), as shown by the variable rooms. Then, as i points to the third start event, we’ll find that this event happens after the end event pointed by endsItr, then we increment endsItr so that it points to the next end event. What happens here can be thought of as one of the two previous meetings ended, and we moved the newly started meeting into that vacant room, thus we don’t need to increment rooms at this time and move both of the pointers forward.
Next, because endsItr moves to the next end event, we’ll find that the start event pointed by i happens before the end event pointed by endsItr. Thus, now we have 4 meetings started but only one ended, so we need one more room. And it goes on as this.
"""

"""
https://i.loli.net/2018/09/24/5ba81e5ea9d15.jpg
https://i.loli.net/2018/09/24/5ba81e7c04aee.jpg
From this simulation, we can see if starts[i] < ends[endItr], we cannot use a room we used before, otherwise we can reuse a room.
"""

TC: Time Complexity: O(Nlog⁡N)
SC: O(N)
    def minMeetingRooms(self, intervals):
        # Sort the given meetings by their start time
        intervals.sort(key=lambda x:x[0])
        #Initialize a new min-heap
        free_rooms = []  # stores the end time of intervals
        for i in intervals:
        # For every meeting room check if the minimum element of the heap i.e. the room at the top of the heap is free or not.
            if free_rooms and i[0] >= free_rooms[0]: 
             #If the current time slot's begin time is larger than the smallest end time in the minimum heap == we don't have overlap == we don't need a new room == we can share the room with the smallest end time in the minimum heap.However, we need to update the minimum heap by using replace method.
             # don't need a new meeting rom  
                heapq.heapreplace(free_rooms, i[1])
            elif free_rooms == [] or i[0] < free_rooms[0]:
            #This condition is inferred. Check could be left 
            #If the current time slot's begin time is less than the smallest end time in the minimum heap, we have an overlap now, i.e., we need a new room, we need to push the current time slot's end time into the minimum heap.
            # keep track of the ending times as that tells us when a meeting room will get free
                heapq.heappush(free_rooms, i[1])
        #After processing all the meetings, the size of the heap will tell us the number of rooms allocated. This will be the minimum number of rooms needed to accommodate all the meetings.
        return len(free_rooms)

    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
           if start[s] < end[e]:
                s + = 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        resturn res


