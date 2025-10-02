class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]: # search space is in the right portion
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            elif nums[mid] == nums[right]: # discard the nums[right] because we already have a copy of it at middle
                right -= 1
        return nums[left]