class Solution:
    def checkRecord(self, n: int) -> int:
        
        MOD = 10 ** 9 + 7
        # dp[a][l]
        dp = [[0] * 3 for _ in range(2)]

        dp[0][0] = 1

        for _ in range(n):
            nxt = [[0] * 3 for _ in range(2)]

            for a in range(2):
                for l in range(3):
                    ways = dp[a][l]
                    if ways == 0:
                        continue
                    
                    nxt[a][0] = (nxt[a][0] + ways) % MOD

                    if a == 0:
                        nxt[1][0] = (nxt[1][0] + ways) % MOD
                    
                    if l < 2:
                        nxt[a][l + 1] = (nxt[a][l + 1] + ways) % MOD
            
            dp = nxt

        ans = 0
        for a in range(2):
            for l in range(3):
                ans = (ans + dp[a][l]) % MOD
        return ans