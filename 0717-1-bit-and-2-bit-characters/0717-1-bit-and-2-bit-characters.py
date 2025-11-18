class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # its either 0, 10, or 11
        prev = None
        curr = ''
        n = len(bits)
        start = 0
        for i, x in enumerate(bits):
            if i == n - 1:
                if prev is None:
                    return True
                else:
                    return False

            if prev == 1 and x == 0:
                start = i + 1
                prev = None
            elif prev == 1 and x == 1:
                start = i + 1
                prev = None
            elif prev is None and x == 1:
                prev = 1
            elif prev is None and x == 0:
                start = i + 1
            




            
