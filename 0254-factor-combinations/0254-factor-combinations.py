class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        
        factors = []
        ans = []
        curr = []
        for x in range(2, n + 1):
            if n % x == 0:
                factors.append(x)

        def backtrack(num, start_idx, curr):

            if num == 1:
                if len(curr) > 1:
                    ans.append(curr[:])
                return   
            
            for i in range(start_idx, len(factors)):
                f = factors[i]
                if num % f == 0:
                    curr.append(f)
                    backtrack(num // f, i, curr)
                    curr.pop()

        backtrack(n, 0, [])
        return ans

        