class Solution:
    def validStrings(self, n: int) -> List[str]:
        
        res, sol = [], []
        def backtrack(i):
            
            if len(sol) == n:
                res.append(''.join(sol[:]))
                return
            
            for x in range(2):
                x = str(x)
                if x == '0' and (sol and sol[-1] == '0'):
                    continue
                sol.append(x)
                backtrack(i + 1)
                sol.pop()

        backtrack(0)
        return res