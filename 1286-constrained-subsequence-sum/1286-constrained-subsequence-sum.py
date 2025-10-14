class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        
        # dp[i] defined as max sum of non empty subsequence of array up to nums[:i] 
        N = len(nums)
        dp = [0] * N
        dp[0] = nums[0]
        ans = dp[0]
        dq = deque([0]) # store indices of decreasing dp

        for j in range(1, N):

            while dq and j - dq[0] > k: # shrink window
                dq.popleft()
            
            best_prev = dp[dq[0]] if dq else 0
            dp[j] = nums[j] + max(0, best_prev)

            while dq and dp[dq[-1]] <= dp[j]:
                dq.pop()
            dq.append(j)
            
            ans = max(ans, dp[j])
        
        return ans

            
