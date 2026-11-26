from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        p=defaultdict(int)
        for i in nums:
            p[i]+=1
        sorted_keys = [key for key, value in sorted(p.items(), key=lambda item: item[1], reverse=True)]
        
        return sorted_keys[:k]
