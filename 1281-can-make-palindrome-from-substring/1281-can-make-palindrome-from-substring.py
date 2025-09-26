class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        N = len(s)
        ALPH = 26

        prefix = [[0] * ALPH for _ in range(N + 1)]

        for i, char in enumerate(s):
            ci = ord(char) - ord('a')

            for c in range(ALPH):
                prefix[i + 1][c] = prefix[i][c]
            
            prefix[i + 1][ci] += 1
        
        ans = []

        for L, R, k in queries:
            odd_count = 0
            for c in range(ALPH):
                cnt = prefix[R + 1][c] - prefix[L][c]
                if cnt % 2 == 1:
                    odd_count += 1
            
            needed = odd_count // 2
            ans.append(needed <= k)
        return ans