class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        M = len(nums2)
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        ans = 0
        for i in range(N - 1, -1, -1):
            for j in range(M - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                    if dp[i][j] > ans:
                        ans = dp[i][j]
        
        return ans