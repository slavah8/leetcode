class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        dp = {}

        words.sort(key = lambda w: len(w))

        dp = {}  # dp[word] = length of longest chain ending at `word`
        best = 1

        for w in words:
            dp[w] = 1

            for i in range(len(w)):
                prev = w[:i] + w[i + 1:]

                if prev in words:
                    dp[w] = max(dp[w], dp[prev] + 1)
                
            best = max(best, dp[w])
        
        return best