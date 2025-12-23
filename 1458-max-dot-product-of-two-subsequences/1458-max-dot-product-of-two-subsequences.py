class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # Let dp[i][j] = maximum dot product using subsequences

        n = len(nums1)
        INF = 10 ** 10
        m = len(nums2)

        dp = [[-INF] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                prod = nums1[i] * nums2[j]
                take = prod

                if dp[i + 1][j + 1] > 0:
                    take = prod + dp[i + 1][j + 1]
                
                dp[i][j] = max(take, dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]


                