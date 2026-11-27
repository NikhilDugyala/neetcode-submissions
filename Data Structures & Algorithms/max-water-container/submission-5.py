class Solution:
    def maxArea(self, heights: List[int]) -> int:
        Max_area = 0
        n = len(heights)
        l = 0
        r = n -1 
        while l<r:
            area = (r-l) * min (heights[l], heights[r])
            Max_area = max(area, Max_area)
            if heights[l]<=heights[r]:
                l+=1
                continue
            if heights[l]>heights[r]:
                r-=1
                continue
        return Max_area

