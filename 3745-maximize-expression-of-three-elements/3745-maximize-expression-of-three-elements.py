class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        
        nums.sort(reverse = True)
        a = nums[0]
        b = nums[1]
        c = nums[-1]

        return a + b - c
        