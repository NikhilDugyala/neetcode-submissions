class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        
        dp = [nums[0], max(nums[0], nums[1])]
        i =2
        while i<n:
            dp[0], dp[1]=  dp[1], max(dp[1], nums[i]+dp[0])
            i+=1
        return dp[-1]



        