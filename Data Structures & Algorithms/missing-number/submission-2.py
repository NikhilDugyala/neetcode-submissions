class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i,j in enumerate(nums):
            n ^= i^j
        return n

        