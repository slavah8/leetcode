class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        
        houses = len(costs)

        colors = len(costs[0])
        INF = 10 ** 15
        dp = [[INF] * colors for _ in range(houses)]

        for c in range(colors):
            dp[0][c] = costs[0][c]
        
        print(dp)

        for i in range(1, houses):
            for color in range(colors):
                best = INF
                for c in range(colors):
                    if c == color:
                        continue
                    
                    cand = dp[i - 1][c]
                    if cand < best:
                        best = cand
                
                dp[i][color] = best + costs[i][color]
        print(dp)

        return min(dp[houses - 1])