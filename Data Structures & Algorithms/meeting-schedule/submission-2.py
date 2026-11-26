"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key= lambda x:x.start)
        i=1
        n=len(intervals)
        counter = (intervals[0].start, intervals[0].end)
        while i<n:
            if counter[1]<=intervals[i].start:
                counter = (intervals[i].start, intervals[i].end)
                i+=1
            else:

                return False
        
        return True
