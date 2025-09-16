class MyCalendar:

    def __init__(self):
        self.delta = defaultdict(int)
        

    def book(self, startTime: int, endTime: int) -> bool:
        self.delta[startTime] += 1
        self.delta[endTime] -= 1

        running = 0
        for x in sorted(self.delta):
            running += self.delta[x]
            if running > 1:
                self.delta[startTime] -= 1
                self.delta[endTime] += 1

                if self.delta[startTime] == 0:
                    del self.delta[startTime]
                if self.delta[endTime] == 0:
                    del self.delta[endTime]
                return False
            
        return True

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)