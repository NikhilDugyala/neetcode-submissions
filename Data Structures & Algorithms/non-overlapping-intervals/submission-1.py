class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        i=1
        n=len(intervals)
        count=0
        prev = intervals[0]

        while i<n:
            if prev[1]>intervals[i][0]:
                prev[1]= min(prev[1], intervals[i][1])
                count+=1
            else:
                prev=intervals[i]
            i+=1
        return count
