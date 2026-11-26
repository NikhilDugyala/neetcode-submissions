class Solution:
    def myPow(self, x: float, n: int) -> float:
        out =1
        if n>0:
            while n!=0:
                out*=x
                n-=1
            return out
        elif n==0:
            return 1
        else:
            while n!=0:
                out*=x
                n+=1
            return 1/out

        