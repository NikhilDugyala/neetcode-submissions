from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = defaultdict(list)
        for i in strs:
            sorted_words = tuple(sorted(i))
            s[sorted_words].append(i)
        
        return list(s.values())




        