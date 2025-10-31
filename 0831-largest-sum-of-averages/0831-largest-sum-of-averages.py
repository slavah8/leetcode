class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)

        pref = [0.0] * (n + 1)
        for i in range(1, n + 1):
            pref[i] = pref[i - 1] + nums[i - 1]
        
        def avg(l, r):
            return (pref[r + 1] - pref[l]) / (r - l + 1)
        # dp[g][i] = best score for the first i elements using exactly g groups.
        dp = [[0.0] * (n + 1) for _ in range(k + 1)]

        # Base: dp[1][i] = average(0..i-1).
        for i in range(1, n + 1):
            dp[1][i] = avg(0, i - 1)
        
        for g in range(2, k + 1): # # g = number of groups
            # need at least g elements to fill g groups
            for i in range(g, n + 1): # # i = prefix length (we solve for first i elements)
                best = 0.0
                #  Last cut at t (so last group is [t..i-1])
                # # t must be >= g-1 so that first g-1 groups have at least g-1 elements.
                for t in range(g - 1, i): # # t = index where the last group starts
                    candidate = dp[g - 1][t] + avg(t, i - 1)
                    if candidate > best:
                        best = candidate
                dp[g][i] = best
        return dp[k][n]

