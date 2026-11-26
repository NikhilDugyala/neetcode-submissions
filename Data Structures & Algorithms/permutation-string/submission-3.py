class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = len(s1)
        for r in range(len(s2)-l+1):
            if sorted(s1)==sorted(s2[r:r+l]):
                return True
        return False
        