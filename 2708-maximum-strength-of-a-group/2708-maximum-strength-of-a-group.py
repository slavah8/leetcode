class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        
        n = len(nums)
        INF = 10 ** 10
        best = -INF
        def backtrack(i, curr_strength, group):
            nonlocal best
            if i == n:
                if len(group) > 0 and curr_strength > best:
                    best = curr_strength
                return
            
            # pick curr student
            group.append(nums[i])
            backtrack(i + 1, curr_strength * nums[i], group)
            group.pop()
            
            # skip curr student
            backtrack(i + 1, curr_strength, group)
        
        backtrack(0, 1, [])
        return best