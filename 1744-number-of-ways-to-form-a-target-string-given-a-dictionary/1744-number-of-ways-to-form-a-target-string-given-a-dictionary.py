class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10 ** 9 + 7
        L = len(words[0])
        # build freq by column
        # freq[k][c] how many words have char c in column k
        freq = [defaultdict(int) for _ in range(L)]
        for w in words:
            for i, char in enumerate(w):
                freq[i][char] += 1


        # DP over columns dp[i] is number of ways to build target[:i]
        M = len(target)
        dp = [0] * (M + 1)
        dp[0] = 1

        for k in range(L): # columns left to right
            for i in range(M, 0, -1):
                char = target[i - 1]
                count = freq[k].get(char, 0)
                if count:
                    dp[i] = (dp[i] + dp[i - 1] * count) % MOD
        
        return dp[M]
