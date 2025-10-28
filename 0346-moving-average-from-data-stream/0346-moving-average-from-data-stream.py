class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = collections.deque()
        

    def next(self, val: int) -> float:
        while len(self.queue) >= self.size:
            self.queue.popleft()
        
        self.queue.append(val)
        return sum(self.queue) / len(self.queue)




        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)