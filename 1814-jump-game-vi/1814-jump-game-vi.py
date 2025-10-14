class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        # Let dp[i] = max score to land on index i.
        # a jump can come from any j in the window i - k <= j < i
        # relate dp[i] = nums[i] + max(dp[j] for j in [i - k, i - 1])

        # use monotnic dq (indices) that keeps dp values in decreasing order

        # when you move to i pop front the front if its out of the window (index < i + k)
        # before pushing i, pop from the back removing dp[back] <= dp[i] to maintain decreasing order

        N = len(nums)
        dp = [0] * N
        dp[0] = nums[0]
        dq = deque([0]) # store indices, decreasing dp

        for i in range(1, N):

            while dq and dq[0] < i - k:
                dq.popleft()
            
            dp[i] = nums[i] + dp[dq[0]]

            while dq and dp[dq[-1]] <= dp[i]: 
                dq.pop()
            dq.append(i)
        
        return dp[N - 1]