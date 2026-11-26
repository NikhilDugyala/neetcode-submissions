class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [0]*len(nums)
        prod,zero_ct = 1,0
        for i in nums:
            if i:
                prod*=i
            else:
                zero_ct+=1
        if zero_ct > 1: return [0] * len(nums)

        for key,value in enumerate(nums):
            if zero_ct: out[key]=0 if value!=0 else prod
            else:
                out[key]=prod//value
        return out
        