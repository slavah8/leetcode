class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        N = len(nums)

        pow3 = [1] * (numSlots + 1)
        for i in range(1, numSlots + 1):
            pow3[i] = pow3[i - 1] * 3
        
        print(pow3)

        # whole board fits into a base 3 mask of length numSlots

        # dp(i, state) : max AND-sum using numbers nums[:i]
        @lru_cache(None)
        def dp(i, state):
            if i == N:
                return 0
            
            best = 0
            x = nums[i]

            # try placing x into any slot with remaining capacity
            for s in range(numSlots):
                used = (state // pow3[s]) % 3
                if used < 2:
                    # increment used for slot s
                    next_state = state + pow3[s]
                    gain = (x & (s + 1)) + dp(i + 1, next_state)
                    if gain > best:
                        best = gain
            return best
        
        return dp(0, 0)