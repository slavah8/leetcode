class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        
        best = 0
        n = len(nums)
        for L in range(n):
            seen_odd = set()
            seen_even = set()
            for R in range(L, n):
                if nums[R] % 2 == 0:
                    seen_even.add(nums[R])
                else:
                    seen_odd.add(nums[R])
                
                if len(seen_even) == len(seen_odd):
                    best = max(best, R - L + 1)
        
        return best

             
