class Solution:
    def reverse(self, x: int) -> int:
        a = abs(x)
        out = int(str(a)[::-1])
        if x <0:
            out*=-1
        if out  < -2**31or out > 2**31 -1:
            return 0
        return out

        