class LUPrefix:

    def __init__(self, N: int):
        self.uploaded = [False] * (N + 2)
        self.ptr = 0
        

    def upload(self, video: int) -> None:
        self.uploaded[video] = True
        while self.uploaded[self.ptr + 1]:
            self.ptr += 1
        

    def longest(self) -> int:
        return self.ptr
        
        

        


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()