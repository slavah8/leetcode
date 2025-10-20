class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        # stack holds the length of the longest nondecreasing suffix ending at index r

        for r, x in enumerate(nums):

            while stack and x < stack[-1]:
                stack.pop()
            stack.append(x)
            ans += len(stack)
        return ans
            
