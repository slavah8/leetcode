class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        
        # dp[i] defined as max substring up to index i in s[:i]

        mapping = {c : v for c, v in zip(chars, vals)}

        print(mapping)
        n = len(s)
        dp = [0] * n
        dp[0] = mapping.get(s[0], ord(s[0]) - ord('a') + 1)
        best = max(0, dp[0])


        for i in range(1, n):
            ch = s[i]
            ch_val = mapping.get(ch, ord(ch) - ord('a') + 1)
            
            dp[i] = max(dp[i - 1] + ch_val, ch_val)
            best = max(best, dp[i])
        
        return best
