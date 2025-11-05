class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        if not self.low or num <= -self.low[0]:
            heapq.heappush(self.low, -num)
        else:
            heapq.heappush(self.high, num)
        
        # rebalance
        if len(self.low) > len(self.high) + 1: # low too big
            num = -heapq.heappop(self.low)
            heapq.heappush(self.high, num)
        elif len(self.high) > len(self.low):
            num = heapq.heappop(self.high)
            heapq.heappush(self.low, -num)
        

    def findMedian(self) -> float:
        if len(self.low) == len(self.high):
            return (-self.low[0] + self.high[0]) / 2.0
        else:
            return float(-self.low[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()