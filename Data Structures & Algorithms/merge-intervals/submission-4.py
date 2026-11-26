class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n= len(intervals)
        intervals.sort(key= lambda x:x[0])
        out = []
        i=0
        current=[intervals[0][0], intervals[0][1]]
        while i<n:
            if current[1]>=intervals[i][0]:
                current[1]=max(current[1],intervals[i][1])
            else:
                out.append(current)
                current= intervals[i]
            i+=1
        out.append(current)

        
        return out





        
