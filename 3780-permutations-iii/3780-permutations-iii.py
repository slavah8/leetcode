class Solution:
    def permute(self, n: int) -> List[List[int]]:
        
        res, perm = [], []
        def backtrack(i):
            if len(perm) == n:
                res.append(perm[:])
                return
            print(perm)
            for x in range(1, n + 1):
                if x in perm:
                    continue
                if (perm and (x % 2 == 0 and perm[-1] % 2 == 0)) or (perm and (x % 2 == 1 and perm[-1] % 2 == 1)):
                    continue
                perm.append(x)
                backtrack(x + 1)
                perm.pop()
        backtrack(1)
        return res
