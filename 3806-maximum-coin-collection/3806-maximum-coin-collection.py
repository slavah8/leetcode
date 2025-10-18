class Solution:
    def maxCoins(self, lane1: List[int], lane2: List[int]) -> int:
        # dp[i][0] = end at i on L1 with 0 switches  (L1)
        # dp[i][1] = end at i on L2 with 1 switch    (L1->L2)
        # dp[i][2] = end at i on L1 with 2 switches  (L1->L2->L1)

        # define dp[i][s] max coins for a segment ending at mile i with state s

        INF = 10 ** 15
        N = len(lane1)
        dp = [[-INF] * (3) for _ in range(N)]

        # i = 0 base case
        dp[0][0] = lane1[0] # start here on lane 1
        dp[0][1] = lane2[0] # start here immediately switch to lane2
        dp[0][2] = -INF # cant switch twice right away

        ans = max(dp[0])

        for i in range(1, N):
            # L1 0 switches either extend or start anew
            dp[i][0] = max(dp[i - 1][0] + lane1[i], lane1[i])
            
            # L2 1 switch switch here, extend here and dont switch, start anew here and switch right away
            dp[i][1] = max((dp[i - 1][0] + lane2[i], dp[i - 1][1] + lane2[i], lane2[i]))

            # end at L1 2 switches : extend here staying at L1, use second switch here
            dp[i][2] = max(dp[i - 1][2] + lane1[i], dp[i - 1][1] + lane1[i])

            ans = max(ans, dp[i][0], dp[i][1], dp[i][2])
        return ans