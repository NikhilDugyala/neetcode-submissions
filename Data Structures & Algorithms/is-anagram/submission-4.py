from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        k = defaultdict(int)

        for i in s:
            k[i]+=1
        
        for j in t:
            k[j]-=1
        
        for key,value in k.items():
            if value!=0:
                return False
        return True
        

        
        