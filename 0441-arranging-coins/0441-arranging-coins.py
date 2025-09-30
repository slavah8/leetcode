class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        need = 1
        rows = 0
        while n >= need:
    
            n -= need
            need += 1
            rows += 1
        return rows
