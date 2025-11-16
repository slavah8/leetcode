class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        n = columnNumber
        res = []
        while n > 0:
            n -= 1
            rem = n % 26
            res.append(chr(rem + ord('A')))
            n //= 26
        return ''.join(reversed(res))
        


