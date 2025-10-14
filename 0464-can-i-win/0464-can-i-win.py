class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        m = maxChoosableInteger
        # win(used_mask, need) = True iff the current player (to move) can force a win given

        total_sum = m * (m + 1) // 2
        if total_sum < desiredTotal:
            return False

        @lru_cache(maxsize = None) 
        def win(bitmask, need):

            for x in range(1, m + 1):
                bit = 1 << (x - 1)
                if bitmask & bit: # already used
                    continue
                
                if x >= need: # if can reach desired total return true
                    return True
                
                next_mask = bitmask | bit
                if not win(next_mask, need - x):
                    return True
                
            return False
        
        return win(0, desiredTotal)


