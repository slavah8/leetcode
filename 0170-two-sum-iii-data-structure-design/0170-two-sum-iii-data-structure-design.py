class TwoSum:

    def __init__(self):
        self.freq = defaultdict(int)
        

    def add(self, number: int) -> None:
        self.freq[number] += 1

        

    def find(self, value: int) -> bool:
        for x, cnt in self.freq.items():
            y = value - x
            if y in self.freq:
                if x != y:
                    return True
                if x == y and self.freq[y] >= 2:
                    return True
        return False



        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)