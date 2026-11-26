class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        start = nums[0]
        total = 0
        for n in nums:
            total+=n
            start = max(start, total)
            if total<0:
                total=0
        return start
