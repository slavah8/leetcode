class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        ops = 0
        score = None
        while len(nums) >= 2:
            x = nums.pop(0)
            y = nums.pop(0)
            
            if score is None:
                score = x + y
            else:
                if x + y != score:
                    return ops
            ops += 1
        
        return ops


            
            