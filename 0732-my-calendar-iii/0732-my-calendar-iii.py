class MyCalendarThree:

    def __init__(self):
        self.delta = defaultdict(int)

    def book(self, startTime: int, endTime: int) -> int:
        self.delta[startTime] += 1
        self.delta[endTime] -= 1

        maxx = 0
        running = 0 
        for x in sorted(self.delta):
            running += self.delta[x]
            maxx = max(maxx, running)
        
        return maxx


        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)