class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        triplets = []
        for i in range(n):
            if nums[i]>0:
                break
            
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            left = i+1
            right = n-1

            while left<right:
                threesum = nums[left]+nums[right]+nums[i]
                if threesum==0:
                    triplets.append([nums[i],nums[left], nums[right]])
                    left+=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                elif threesum<0:
                    left+=1
                elif threesum>0:
                    right-=1
        return triplets
        