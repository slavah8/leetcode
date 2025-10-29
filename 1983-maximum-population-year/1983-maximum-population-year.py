class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        diff = [0] * 102
        for s, e in logs:
            # 1950 mapped to 0 
            # 2050 mapped to 100
            L = s - 1950
            R = e - 1950
            diff[L] += 1
            diff[R] -= 1
        
        print(diff)
        prefix = [0] * 103
        for i, x in enumerate(diff):
            prefix[i + 1] = prefix[i] + x
        
        print(prefix)
        maxx = max(prefix)
        max_idx = prefix.index(maxx)
        return 1950 + max_idx - 1
