"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        n=len(intervals)
        # add all the start and end interval time to their arrays and sort
        s,e = [], []
        for i in range(n):
            s.append(intervals[i].start)
        for i in range(n):
            e.append(intervals[i].end)
        i=0
        j=0

        s.sort()
        e.sort()
        print(s)
        print(e)
        out=0
        count=0
        while i<n and j<n:
            print("Stating i",i)
            print("Stating i",j)

            print("starting s[i], e[i]",s[i], e[j])
            if s[i]<e[j]:
                count+=1
                print("count", count)
                i+=1
            else:
                print("else", s[i], e[j])
                count-=1
                j+=1
                print("count else", count)
            
            out=max(out,count)
            print("out", out)

        return out



