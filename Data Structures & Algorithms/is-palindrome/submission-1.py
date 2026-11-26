class Solution:
    def isPalindrome(self, s: str) -> bool:
        d = "".join(ch.lower() for ch in s if ch.isalnum())
        for i in range(len(d)//2):
            if d[i] != d[len(d)-i-1]:
                return False
        return True
        