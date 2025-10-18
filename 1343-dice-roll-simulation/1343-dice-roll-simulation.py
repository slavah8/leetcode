class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7

        K = max(rollMax)
        m = 6
        # dp[i][f][k] = number of length-i sequences where the last roll is face f and the current run of f has length k
        prev = [[0] * (K + 1) for _ in range(m)]

        for f in range(m):
            prev[f][1] = 1
        
        # returns rowSum and total
        def compute_sums(layer):
            rowSum = [0] * m
            total = 0
            for f in range(m):
                s = 0
                for k in range(1, rollMax[f] + 1):
                    s += layer[f][k]
                s %= MOD
                rowSum[f] = s
                total = (total + s) % MOD
            return rowSum, total

        rowSum, total = compute_sums(prev)

        for i in range(2, n + 1):
            cur = [[0] * (K + 1) for _ in range(m)]

            for f in range(m):
                # case 1: switches to f run becomes 1
                # all sequences of length i - 1 minus those already ending with f
                cur[f][1] = (total - rowSum[f]) % MOD # rowSum[f] total number of sequences that end with face f
            
                for k in range(2, rollMax[f] + 1):
                    # case 2: extend same face f (k increases by 1)
                    cur[f][k] = prev[f][k - 1]
            
            prev = cur
            rowSum, total = compute_sums(prev)
        
        if n == 1:
            return total % MOD
        return total % MOD
