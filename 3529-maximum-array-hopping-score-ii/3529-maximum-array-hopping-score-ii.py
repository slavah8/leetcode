class Solution:
    def maxScore(self, nums: List[int]) -> int:
        N = len(nums)
        stack = []

        for i in range(N - 1, -1, -1):
            if not stack or nums[i] > nums[stack[-1]]:
                stack.append(i)
        
        checkpoints = reversed(stack)
        score = 0
        i = 0
        for idx in checkpoints:
            score += (idx - i) * nums[idx]
            i = idx
        return score
