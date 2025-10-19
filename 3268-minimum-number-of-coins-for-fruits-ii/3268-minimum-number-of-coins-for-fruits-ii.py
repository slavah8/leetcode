class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        if len(prices) == 0 or prices[0] != 0:
            prices = [0] + prices
        n = len(prices) - 1
        INF = 10 ** 15
        dq = deque() # holds index j minimum number of coins so far
        dp = [INF] * (n + 1)
        dq.append(0) 
        dp[0] = 0
        val = [0] * (n + 1) # Cost of a plan that ends by buying fruit j right now.
         
        for t in range(1, n + 1):

            # add the new right endpoint j = t into deque
            val[t] = dp[t - 1] + prices[t]
            while dq and val[dq[-1]] >= val[t]:
                dq.pop()
            dq.append(t)

            lo = math.ceil(t / 2) # left bound
            # shrink window for only valid j's [math.ceil(t /2), t]
            while dq and dq[0] < lo:
                dq.popleft()
            
            dp[t] = val[dq[0]]
        
        return dp[n]

