class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])

        deleted = 0

        fixed = [False] * (n - 1)

        for c in range(m):
            bad = False
            for i in range(n - 1):
                if not fixed[i] and strs[i][c] > strs[i + 1][c]:
                    bad = True
                    break
            
            if bad:
                deleted += 1
                continue
            
            for i in range(n - 1):
                if not fixed[i] and strs[i][c] < strs[i + 1][c]:
                    fixed[i] = True
            
            if all(fixed):
                break
        return deleted

