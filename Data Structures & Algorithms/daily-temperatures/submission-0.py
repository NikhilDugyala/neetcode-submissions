class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        arra = [0]*n
        for i in range(n):
            for j in range (i+1,n):
                if temperatures[j]>temperatures[i]:
                    arra[i]=j-i
                    break
        return arra


        