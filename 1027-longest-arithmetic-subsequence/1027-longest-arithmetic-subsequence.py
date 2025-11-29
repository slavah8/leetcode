class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        
        # dp[i][d] defined as the longest arithmetic subsuquence at index i and seq diff of d
        ans = 0

        dp = [defaultdict(int) for _ in range(n)]
        print(dp)
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                prev_len = dp[j][diff] if diff in dp[j] else 1
                curr_len = prev_len + 1
                
                if curr_len > dp[i][diff]:
                    dp[i][diff] = curr_len

                if curr_len > ans:
                    ans = curr_len
        return ans