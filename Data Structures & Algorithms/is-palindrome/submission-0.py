class Solution:
    def isPalindrome(self, s: str) -> bool:
        d = "".join(ch.lower() for ch in s if ch.isalnum())
        print(d)
        print(d[::-1])
        return d==d[::-1]
        