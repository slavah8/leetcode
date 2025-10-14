class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        # Let dp[i:] be the maximum score difference the current player (to move at index i) can force 
        # over the opponent using stones i..n-1.

        # on my turn you can take stones k = {1,2,3} 
        # reccurence = 
        N = len(stoneValue) 
        INF = 10 ** 10
        dp = [0] * (N + 1)


        for i in range(N - 1, -1, -1):
            best = -INF
            take = 0
            # take 1
            take += stoneValue[i]
            best = max(best, take - dp[i + 1])

            # take 2
            if i + 1 < N:
                take += stoneValue[i + 1]
                best = max(best, take - dp[i + 2])
            
            # take 3
            if i + 2 < N:
                take += stoneValue[i + 2]
                best = max(best, take - dp[i + 3])
            dp[i] = best
        
        if dp[0] == 0:
            return "Tie"
        elif dp[0] > 0:
            return "Alice"
        else:
            return "Bob"


