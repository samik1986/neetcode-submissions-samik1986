class MedianFinder:

    def __init__(self):
        self.val =  []
        

    def addNum(self, num: int) -> None:
        self.val.append(num)
        

    def findMedian(self) -> float:
        self.val.sort()
        n = len(self.val)
        if n % 2 :  return self.val[n // 2]
        else: return (self.val[n // 2] + self.val[n // 2 - 1])/2
        
        