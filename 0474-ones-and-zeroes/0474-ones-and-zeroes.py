class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        k = len(strs)
        costs = []

        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')
            costs.append((zeros, ones))

        # dp defined as best using first i items within budget
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(k + 1)]


        for i in range(1, k + 1):
            cz, co = costs[i - 1]
            for z in range(0, m + 1):
                for o in range(0, n + 1):
                    # skip this item
                    best = dp[i - 1][z][o]

                    # take this item
                    if z >= cz and o >= co:
                        candidate = 1 + dp[i - 1][z - cz][o - co]
                        if candidate > best:
                            best = candidate
                    
                    dp[i][z][o] = best
        return dp[k][m][n]

            
            