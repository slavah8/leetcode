class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        left = 0
        best = 0
        N = len(nums)
        count = 0
        for right, x in enumerate(nums):
            if x == 1:
                count += 1
                best = max(best, count)
            else:
                count = 0
        return best

            

            

