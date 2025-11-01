class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        
        stack = []
        n = len(nums)
        for i, x in enumerate(nums):
            if not stack or x > nums[stack[-1]]:
                stack.append(i)
        
        ans = 0
        for j in range(n - 1, -1, -1):
            while stack and nums[j] < nums[stack[-1]]:
                i = stack.pop()
                ans = max(ans, j - i + 1)
        return ans
