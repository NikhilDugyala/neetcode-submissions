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
        while slow!=fast:
            slow = sum_of_squares(slow)
            fast = sum_of_squares(sum_of_squares(fast))
        return True if fast ==1 else False


        