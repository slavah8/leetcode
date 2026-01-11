class Solution:
    def newInteger(self, n: int) -> int:
        
        res = 0
        place = 1

        while n > 0:
            digit = n % 9
            res += digit * place
            place *= 10
            n = n // 9
        
        return res