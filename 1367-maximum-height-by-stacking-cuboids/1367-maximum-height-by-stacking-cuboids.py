class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        
        
        for c in cuboids:
            c.sort()
        
        cuboids.sort()
        N = len(cuboids)
        dp = [0] * N  # dp[i] = max total height ending with cuboid i on top
        ans = 0
        for i in range(N):
            a_i, b_i, c_i = cuboids[i]
            dp[i] = c_i # at least the height
            for j in range(i):
                a_j, b_j, c_j = cuboids[j]
                if a_j <= a_i and b_j <= b_i and c_j <= c_i:
                    dp[i] = max(dp[i], c_i + dp[j])
            ans = max(dp[i], ans)
        print(dp)
        return ans
