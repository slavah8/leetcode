class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        # first element to appear exactly once will have an even index
        # # if odd index compare mid with mid - 1
        # if even index compare with mid + 1
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1: 
                mid -= 1
            if nums[mid] == nums[mid + 1]: # all pairs are validly aligned so the search space is to the right
                left = mid + 2
            else: # there was a pair that was not aligned before mid
                right = mid
        return nums[left]
            
            