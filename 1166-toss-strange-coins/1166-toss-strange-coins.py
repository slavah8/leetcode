class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        N = len(prob)

        # dp[i][j] probability that in the first i elements j of them are facing heads

        # relate dp[i][j] = dp[i - 1][]
        """

        """
        dp = [[0] * (N + 1) for _ in range(N + 1)]
        dp[0][0] = 1.0
        

        #dp[2][1] = dp[1][1] * (1 - prob[1]) + (dp[1][0] + prob[1])
        #dp[3][1] = dp[2][1] * (1 - prob[2]) + (dp[2][0] + prob[2])
        # relation : dp[i][j] = dp[i - 1][j] * (1 - prob[i - 1]) + dp[i - 1][j - 1] * prob[i - 1]

        #dp[3][3] dp[2][2] * prob[2]
        #if j > i:
        #    probability = 0 dp = 0

        for i in range(1, N + 1):
            p = prob[i - 1]
            dp[i][0] = dp[i - 1][0] * (1.0 - p)
            for j in range(1, i + 1):
                dp[i][j] = (dp[i - 1][j] * (1.0 - p)) + (dp[i - 1][j - 1] * p)
       
        
        return dp[N][target]



