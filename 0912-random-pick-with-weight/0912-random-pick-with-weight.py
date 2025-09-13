class Solution:

    def __init__(self, w: List[int]):
        self.pref = []
        s = 0
        for x in w:
            s += x
            self.pref.append(s)
        self.total = s

    def pickIndex(self) -> int:
        r = random.randint(1, self.total)
        index = bisect.bisect_left(self.pref, r)
        return index
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()