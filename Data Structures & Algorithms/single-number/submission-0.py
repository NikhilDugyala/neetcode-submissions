class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        p=0
        for i in range(len(nums)):
            p= nums[i]^p
        return p
        