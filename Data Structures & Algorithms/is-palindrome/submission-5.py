class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        s= s.lower()
        while left<right:
            if s[left] != s[right] and s[left].isalnum() and s[right].isalnum():
                return False
            if not(s[left].isalnum()):
                left+=1
                continue
            if not(s[right].isalnum()):
                right-=1
                continue
            left+=1
            right-=1
        return True


        