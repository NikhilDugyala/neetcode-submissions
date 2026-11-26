class Solution:
    def isHappy(self, n: int) -> bool:

        def sum_of_squares(n):
            total =0
            while n>0:
                i = n%10
                total+= i*i
                n//=10
            return total
        slow , fast = n, sum_of_squares(n)
        if fast==1 or slow ==1:
            return True
        while slow!=fast:
            slow = sum_of_squares(slow)
            fast = sum_of_squares(sum_of_squares(fast))
            if fast==1 or slow ==1:
                return True

        return False


        