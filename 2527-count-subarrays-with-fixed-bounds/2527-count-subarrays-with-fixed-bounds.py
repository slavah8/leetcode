class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
    
        last_min = -1
        last_max = -1
        total = 0
        left = 0
        for right, x in enumerate(nums):
            if x > maxK or x < minK:
                last_min = -1
                mast_max = -1
                left = right + 1
                continue
            
            if x == minK:
                last_min = right
            if x == maxK:
                last_max = right
            # earliest index in which both have appearead
            need = min(last_min, last_max)
            if need >= left:
                total += need - left + 1
        return total
            
            
