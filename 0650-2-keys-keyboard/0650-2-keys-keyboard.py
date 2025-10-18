class Solution:
    def minSteps(self, n: int) -> int:
        
        # A
        # dp[i] min number of operations to get A i times on the screen
        INF = 10 ** 10
        dp = [INF] * (n + 1)
        dp[1] = 0
        
        # 1) If i can be written as i = a × b, then we could get to i in two possible ways
        # Finish building a first, then multiply by b:
        # build a in dp[a] operations 
        # then one copy + (b−1) pastes = b operations
        # total = dp[a] + b
        # 2) Finish building b first, then multiply by a
        # build b in dp[b] operations,
        # then one copy + (a−1) pastes = a operations
        # total = dp[b] + a
        for i in range(2, n + 1):
            dp[i] = i
            j = 2
            while j * j <= i:
                if i % j == 0:
                    a = j           # one factor
                    b = i // j      # the paired factor

                    option1 = dp[a] + b 
                    option2 = dp[b] + a
                    dp[i] = min(dp[i], option1, option2)
                j += 1
        return dp[n]
                    


        