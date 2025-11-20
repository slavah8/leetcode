class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        n = len(nums)
        stack = []
        nge = [-1] * n
        INF = 10 ** 10
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            
            if stack:
                nge[i] = stack[-1]
            
            stack.append(i)
        print(nge)

        stack = []
        nse = [-1] * n
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                nse[i] = stack[-1]
            stack.append(i)
        print(nse)

        # dp[x] : min cost to reach index x
        dp = [INF] * n
        dp[0] = 0 

        for i in range(n):
            if dp[i] == INF:
                continue
            
            # from i we can jump to nge[i] or nse[i]
            if nge[i] != -1:
                j = nge[i]
                dp[j] = min(dp[j], dp[i] + costs[j])
            if nse[i] != -1:
                k = nse[i]
                dp[k] = min(dp[k], dp[i] + costs[k])

        print(dp)
        return dp[n - 1]