class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        
        """
        move left-to-right. Among all intervals that start at or before the current covered end, pick the one that 
        pushes the covered end farthest right. Repeat.
        """

        best = [0] * (n + 1) # farthest right any tap that starts at L can reach

        for i, r in enumerate(ranges):
            if r == 0:
                continue
            
            L = max(0, i - r)
            R = min(n, i + r)
            best[L] = max(best[L], R)
        

        ans = 0
        # curr_end: the rightmost position currently covered by the taps you’ve committed (opened).
        # After opening ans taps, you have coverage [0..curr_end].
        curr_end = 0 
        # next_end: the farthest position you could reach if you open one more tap 
        # among those that start within your current coverage
        next_end = 0

        for x in range(n + 1):
            
            if x > next_end:
                return -1
            
            if x > curr_end: # stepped beyond coverage
                ans += 1
                curr_end = next_end
            
            # extend next frontier 
            next_end = max(next_end, best[x])
        
        return ans
