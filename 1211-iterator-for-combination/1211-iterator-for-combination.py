class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []
        self.comb = []
        self.index = 0
        def backtrack(i, length):
            if length == combinationLength:
                self.combinations.append(''.join(self.comb[:]))
                return
            if i == len(characters):
                return
            
            # include
            self.comb.append(characters[i])
            backtrack(i + 1, length + 1)
            self.comb.pop()
            # dont include
            backtrack(i + 1, length)

        backtrack(0, 0)
        print(self.combinations)



    def next(self) -> str:
        ans = self.combinations[self.index]
        self.index += 1
        return ans

    def hasNext(self) -> bool:
        if self.index < len(self.combinations):
            return True
        else:
            return False
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()