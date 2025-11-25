class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        total = sum(chalk)
        k %= total
        i = 0
        n = len(chalk)
        
        while k >= 0:
            if k < chalk[i]:
                return i
            
            k -= chalk[i]
            
            i += 1
            if i == n:
                i = 0
            