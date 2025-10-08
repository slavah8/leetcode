class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        # dp[i] = max sub array length up to index i with positive product
        N = len(nums)
        neg = 0
        pos = 0
        best = 0
        for x in nums:
            if x == 0:
                pos = 0
                neg = 0
            elif x > 0: # if positive
                pos = pos + 1
                neg = neg + 1 if neg > 0 else 0
            else: # negative
                new_pos = neg + 1 if neg > 0 else 0
                new_neg = pos + 1
                pos, neg = new_pos, new_neg
            best = max(best, pos)
        return best
                

                



