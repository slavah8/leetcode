class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        
        n = len(aliceArrows)
        best = 0
        
        ans = None
        def backtrack(i, remaining, curr, score):
            nonlocal best, ans
            
            if remaining == 0:
                if score > best:
                    best = score
                    ans = curr[:]
                return

            if i == n:
                if score > best:
                    best = score
                    ans = curr[:]
                return
            
            
            # shoot here
            if remaining >= aliceArrows[i] + 1:
                curr[i] = aliceArrows[i] + 1
                backtrack(i + 1, remaining - curr[i], curr, score + i)
                curr[i] = 0

            # skip shooting here
            backtrack(i + 1, remaining, curr, score)

        backtrack(0, numArrows, [0] * n, 0)

        leftover = numArrows - sum(ans)
        print(leftover)
        for i, x in enumerate(ans):
            if x != 0:
                ans[i] += leftover
                break
                
        return ans
