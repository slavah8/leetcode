class Logger:

    def __init__(self):
        self.string_to_time = defaultdict(int)
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.string_to_time:
            self.string_to_time[message] = timestamp
            return True
        else:
            if self.string_to_time[message] + 10 <= timestamp:
                self.string_to_time[message] = timestamp
                return True
            else:
                return False

        
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)