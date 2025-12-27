class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        # Let dp(op, l) be: maximum score achievable after performing op operations, where l of those picks came from the left.
        @lru_cache(None)
        def dp(ops, l):
            if ops == m:
                return 0

            r = n - 1 - (ops - l)
            # if we take ops and l from the left then the leftmost index is l
            take_left = multipliers[ops] * nums[l] + dp(ops + 1, l + 1)

            take_right = multipliers[ops] * nums[r] + dp(ops + 1, l)
            
            return max(take_left, take_right)


        return dp(0, 0)