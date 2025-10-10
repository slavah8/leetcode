class Solution:
    def checkPartitioning(self, s: str) -> bool:
        N = len(s)
        # dp[i][j] defined as True if the substring s[i:j] is a palindome
        pal = [[False] * N for _ in range(N)]

        for i in range(N):
            pal[i][i] = True
        for i in range(N - 1):
            if s[i] == s[i + 1]:
                pal[i][i + 1] = True


        
        for length in range(3, N + 1):
            for i in range(N - length + 1):
                j = i + length - 1
                if s[i] == s[j] and pal[i + 1][j - 1]:
                    pal[i][j] = True
        
        firstPalEnd = [pal[0][i] for i in range(N)]
        print(firstPalEnd)
        good2 = [False] * N # Can the prefix s[0..j] be split into two palindromic substrings
        for j in range(1, N): # end of second piece
            ok = False
            for i in range(0, j):
                if firstPalEnd[i] and pal[i + 1][j]:
                    ok = True
                    break
            good2[j] = ok
        
        for j in range(1, N - 1):
            if good2[j] and pal[j + 1][N - 1]:
                return True
        return False

