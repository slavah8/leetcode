class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.i = 0 # v1 pointer
        self.j = 0 # v2 pointer
        self.parity = 0

    def next(self) -> int:
        if self.parity == 0 and self.i < len(self.v1): # v1 turn
            tmp = self.v1[self.i]
            self.i += 1
            self.parity = 1 if self.j < len(self.v2) else 0
            return tmp
        else:
            tmp = self.v2[self.j]
            self.j += 1
            self.parity = 0 if self.i < len(self.v1) else 1
            return tmp

        
        

    def hasNext(self) -> bool:
        if self.i < len(self.v1) or self.j < len(self.v2):
            return True
        return False
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())