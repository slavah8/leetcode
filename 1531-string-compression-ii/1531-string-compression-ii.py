class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        INF = 10 ** 10
        n = len(s)

        def run_len(cnt):
            if cnt == 1:
                return 1
            
            if cnt < 10:
                return 2
            if cnt < 100:
                return 3
            return 4

        # Let dp[i][k] = minimum compressed length for suffix s[i:] if you can delete at most k characters.
        @lru_cache(None)
        def dp(i, k):
            if k < 0:
                return INF
            
            if i >= n or n - i <= k:
                return 0 # can delete everything
            
            # option 1 : delete s[i]
            best = dp(i + 1, k - 1)

            # option 2 : keep s[i] and build a run

            same = 0
            deleted = 0
            for j in range(i, n):

                if s[i] == s[j]:
                    same += 1
                else:
                    deleted += 1
                    if deleted > k:
                        break # invalid
                
                best = min(best, run_len(same) + dp(j + 1, k - deleted))

            return best
        return dp(0, k)