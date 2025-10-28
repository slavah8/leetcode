class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        # 1) Precompute overlaps: ov[i][j] = max suffix of words[i] that matches prefix of words[j]
        ov = [[0]*n for _ in range(n)]

        
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                a, b = words[i], words[j]
                maxk = min(len(a), len(b))
                for k in range(maxk, 0, -1):
                    if a.endswith(b[:k]):
                        ov[i][j] = k
                        break

        # We number words 0..n-1
        # mask is a bitmask of which words are already included in the built superstring.
        # dp[mask][j] = the minimum possible length of a superstring
        # that uses exactly the set of words in mask and whose last word is j
        FULL = 1 << n
        INF = 10 ** 10
        dp = [[INF] * n for _ in range(FULL)]
        parent = [[-1] * n for _ in range(FULL)]

        # base case: the best superstring is the word itself
        for j in range(n):
            dp[1 << j][j] = len(words[j])
        
        for mask in range(FULL):
            for j in range(n):
                # relation
                # We want to end at j with set mask. The previous state must have
                # used exactly pmask mask without j 
                # and ended at some i in pmask
                # try all such i
                if not (mask & (1 << j)):
                    continue
                pmask = mask ^ (1 << j)
                if pmask == 0:
                    continue
                
                # try coming to j from i
                for i in range(n):
                    if i == j or not (pmask & (1 << i)):
                        continue
                    cand = dp[pmask][i] + (len(words[j]) - ov[i][j])
                    if cand < dp[mask][j]:
                        dp[mask][j] = cand
                        parent[mask][j] = i
            

        mask = FULL - 1
        end = min(range(n), key = lambda j: dp[mask][j])
        order = []
        while end != -1:
            order.append(end)
            prev = parent[mask][end]
            mask ^= (1 << end)
            end = prev
        order.reverse()

        ans = words[order[0]]
        for x, y in zip(order, order[1:]):
            ans += words[y][ov[x][y]:]
        return ans


