class StringIterator:

    def __init__(self, s: str):
        self.string1 = ''
        self.j = 0
        i = 0
        count = 0
        letter = ''
        while i < len(s):
            if s[i].isalpha():
                letter = s[i]
                i += 1
            else:
                k = i
                while k < len(s) and s[k].isdigit():
                    k += 1
                count = int(s[i:k])
                self.string1 += (letter * count)
                i = k
                
        self.n = len(self.string1)
        

    def next(self) -> str:
        if self.j < self.n:
            tmp = self.string1[self.j]
            self.j += 1
            return tmp
        else:
            return ' '
        
        

    def hasNext(self) -> bool:
        if self.j < self.n:
            return True
        else:
            return False
        
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()