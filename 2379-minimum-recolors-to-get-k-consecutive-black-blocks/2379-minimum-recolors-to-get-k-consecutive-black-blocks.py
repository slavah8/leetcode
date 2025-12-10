class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        longest = 0

        l = 0
        n = len(blocks)
        window_size = k
        blacks = 0
        for i in range(k):
            if blocks[i] == 'B':
                blacks += 1
        
        best = k - blacks
        
        l = 0
        for r in range(k, n):
            if blocks[r] == 'B':
                blacks += 1
            
            if blocks[l] == 'B':
                blacks -= 1
            l += 1
            
            best = min(best, k - blacks)
        return best
        
            



