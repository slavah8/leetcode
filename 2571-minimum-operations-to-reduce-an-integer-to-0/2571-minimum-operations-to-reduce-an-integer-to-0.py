class Solution:
    def minOperations(self, n: int) -> int:
        
        ops = 0
        while n != 0:
            if (n & 1) == 0:
                n = n >> 1
            else:
                if n == 1:
                    ops += 1
                    break
                
                if (n & 3) == 1:
                    n -= 1
                else:
                    n += 1
                
                ops += 1
        return ops