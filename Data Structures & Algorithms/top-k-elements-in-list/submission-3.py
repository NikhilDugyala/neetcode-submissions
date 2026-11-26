from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s= defaultdict(int)
        out = []
        for i in nums:
            s[i]+=1
        
        sorted_dict = sorted(s.items(), key=lambda k:k[1], reverse= True)
        sorted_keys = [key for key,value in sorted_dict]
        return sorted_keys[:k]

        
        