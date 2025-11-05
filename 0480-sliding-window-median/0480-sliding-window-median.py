class DualHeap:
    def __init__(self, k):
        self.k = k
        self.low = []
        self.high = []
        self.to_del = defaultdict(int)
        self.size_low = 0
        self.size_high = 0

    def prune(self, heap):
        while heap:
            x = -heap[0] if heap is self.low else heap[0]
            if self.to_del[x] > 0:
                heapq.heappop(heap)
                self.to_del[x] -= 1
            else:
                break

    def rebalance(self):
        if self.size_low > self.size_high + 1:
            val = -heapq.heappop(self.low)
            self.size_low -= 1
            heapq.heappush(self.high, val)
            self.size_high += 1
            self.prune(self.low)
        elif self.size_high > self.size_low:
            val = heapq.heappop(self.high)
            self.size_high -= 1
            heapq.heappush(self.low, -val)
            self.size_low += 1
            self.prune(self.high)
    
    def add(self, x):
        if not self.low or x <= -self.low[0]:
            heapq.heappush(self.low, -x)
            self.size_low += 1
        else:
            heapq.heappush(self.high, x)
            self.size_high += 1
        self.rebalance()
    
    def erase(self, x):
        self.to_del[x] += 1
        if self.low and x <= -self.low[0]:
            self.size_low -= 1
            if self.low and x == -self.low[0]:
                self.prune(self.low)
        else:
            self.size_high -= 1
            if self.high and x == self.high[0]:
                self.prune(self.high)
        self.rebalance()
    
    def median(self):
        if self.k % 2 == 1:
            self.prune(self.low)
            return float(-self.low[0])
        else:
            self.prune(self.low)
            self.prune(self.high)
            return (-self.low[0] + self.high[0]) / 2.0
    

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        dh = DualHeap(k)
        res = []

        for i in range(k):
            dh.add(nums[i])
        res.append(dh.median())
    
        for i in range(k, len(nums)):
            dh.erase(nums[i - k])
            dh.add(nums[i])
            res.append(dh.median())
        return res
        
