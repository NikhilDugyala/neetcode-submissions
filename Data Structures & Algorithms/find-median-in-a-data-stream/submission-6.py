class MedianFinder:

    def __init__(self):
        self.s = []
        

    def addNum(self, num: int) -> None:
        self.s.append(num)
        

    def findMedian(self) -> float:
        self.s= sorted(self.s)
        k = len(self.s)
        mid = k//2
        if k %2 !=0:
            return float(self.s[mid])
        else:
            return (self.s[mid-1]+self.s[mid])/ 2.0
    
        
        