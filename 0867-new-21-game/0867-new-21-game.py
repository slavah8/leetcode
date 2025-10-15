class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        

        # dp[x] = P(ending with exactly x points) 
        # we only care for 0 <= x <= n
        # how can we reach x
        # To finish with exactly x, the last draw must have come from 
        # some smaller total i (i < k, since you must have been active)
        # You then added a draw d between 1 and W so that: x = i + d
        # Each draw outcome has equal probability 1/W
        # the probability to reach x = average of probabilities of 
        # being at the last W possible previous scores (that were still < k)

        # windowSum = sum of all dp[i] for i in the current window of possible 
        # previous totals that can still draw (i < k).
        
        dp = [0.0] * (n + 1)
        dp[0] = 1
        W = maxPts
        windowSum = 1.0
        ans = 0.0
        if k == 0 or n >= k - 1 + W:
            return 1.0
        # x = the total points we might end up with
        for x in range(1, n + 1):
            
            dp[x] = windowSum / W

            if x < k: # we can still draw from here
                windowSum += dp[x]
            else:
                # x is terminal so add the probability to the ans
                ans += dp[x]
            
            if x - W >= 0 and x - W < k:
                windowSum -= dp[x - W]
        
        return ans
            


            




