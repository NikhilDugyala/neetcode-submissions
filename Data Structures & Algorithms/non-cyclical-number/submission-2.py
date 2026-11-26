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
        while slow!= 1 and fast!=1:
            slow = sum_of_squares(slow)
            print("slow",slow)
            fast = sum_of_squares(sum_of_squares(fast))
            print("fast",fast)
            if slow == fast:
                return slow==1
        return True


        