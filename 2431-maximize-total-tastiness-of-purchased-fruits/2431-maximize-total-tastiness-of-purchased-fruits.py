class Solution:
    def maxTastiness(self, price: List[int], tastiness: List[int], maxAmount: int, maxCoupons: int) -> int:
        
        n = len(price)
        INF = 10 ** 15
        # Let dp[a][c] = maximum tastiness achievable with:
        # total cost exactly a, using exactly c coupons
        dp = [[-INF] * (maxCoupons + 1) for _ in range(maxAmount + 1)]
        dp[0][0] = 0

        for p, t in zip(price, tastiness):
            half = p // 2
            for a in range(maxAmount, -1, -1):
                for c in range(maxCoupons, -1, -1):
                    if dp[a][c] == -INF:
                        continue
                    # buy full
                    if p + a <= maxAmount:
                        dp[p + a][c] = max(dp[p + a][c], t + dp[a][c])
                    
                    # buy with coupon
                    
                    if p != 0 and c + 1 <= maxCoupons and half + a <= maxAmount:
                        dp[a + half][c + 1] = max(dp[a + half][c + 1], t + dp[a][c])
        
        ans = 0
        for a in range(maxAmount + 1):
            for c in range(maxCoupons + 1):
                ans = max(ans, dp[a][c])
        
        return ans
                    


                    





            
            




