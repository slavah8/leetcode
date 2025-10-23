class Solution:
    def splitString(self, s: str) -> bool:
        N = len(s)
        def dfs(i, prev, pieces):
            if i == N:
                return pieces >= 2
            
            num = 0
            for j in range(i, N):
                num = num * 10 + (ord(s[j]) - ord('0'))
                if prev is None:
                    # first piece: ensure at least one char remains for the second piece
                    if j == N - 1:
                        continue
                    if dfs(j + 1, num, pieces + 1):
                        return True
                else:
                    if num >= prev:
                        break
                    if prev - 1 == num:
                        if dfs(j + 1, num, pieces + 1):
                            return True
                        
            return False
        return dfs(0, None, 0)