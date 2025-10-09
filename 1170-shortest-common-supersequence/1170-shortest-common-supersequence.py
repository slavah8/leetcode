class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        N = len(str1)
        M = len(str2)
        LCS = [[0] * (M + 1) for _ in range(N + 1)]

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if str1[i - 1] == str2[j - 1]:
                    LCS[i][j] = 1 + LCS[i - 1][j - 1]
                else:
                    LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])
        
        i = N
        j = M
        res = []
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                res.append(str1[i - 1])
                i -= 1
                j -= 1
            elif LCS[i - 1][j] >= LCS[i][j - 1]:
                res.append(str1[i - 1])
                i -= 1
            else:
                res.append(str2[j - 1])
                j -= 1
        while i > 0:
            res.append(str1[i - 1])
            i -= 1
        while j > 0:
            res.append(str2[j - 1])
            j -= 1
        return ''.join(reversed(res))

