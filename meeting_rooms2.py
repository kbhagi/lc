class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = [] # Create 2 arrays starts and ends to store the each start and end intervals separately.
        ends = []
        rooms, ends_itr = 0,0  # rooms is the variable that would be returned
        for i in intervals:  # Iterating through the 2D intervals, store all the start intervals into a into starts arrays and ends intervals into ends arrray
            starts.append(intervals[i][0])
            ends.append(intervals[i][-1])
        starts.sort() #
        ends.sort()
        for i in starts:
            if starts[i] < ends[ends_itr]:
                rooms+=1
            else:
                ends_itr+=1
        return rooms



The numbers of the intervals give chronological orders
When an ending event occurs, there must be a starting event has happened before that, where “happen before” is defined by the chronological orders given by the intervals
Meetings that started which haven’t ended yet have to be put into different meeting rooms, and the number of rooms needed is the number of such meetings.Initially, endsItr points to the first end event, and we move i which is the start event pointer. As we examine the start events, we’ll find the first two start events happen before the end event that endsItr points to, so we need two rooms (we magically created two rooms), as shown by the variable rooms. Then, as i points to the third start event, we’ll find that this event happens after the end event pointed by endsItr, then we increment endsItr so that it points to the next end event. What happens here can be thought of as one of the two previous meetings ended, and we moved the newly started meeting into that vacant room, thus we don’t need to increment rooms at this time and move both of the pointers forward.
Next, because endsItr moves to the next end event, we’ll find that the start event pointed by i happens before the end event pointed by endsItr. Thus, now we have 4 meetings started but only one ended, so we need one more room. And it goes on as this.


https://i.loli.net/2018/09/24/5ba81e5ea9d15.jpg
https://i.loli.net/2018/09/24/5ba81e7c04aee.jpg
From this simulation, we can see if starts[i] < ends[endItr], we cannot use a room we used before, otherwise we can reuse a room.

#intervals = [[0,30],[5,10],[15,20]], output =2
# intervals = [[7,10],[2,4]], output = 1

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