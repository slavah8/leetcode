class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        N = len(nums)

        # maxima

        PGE = [-1] * N
        NGE = [N] * N

        # find previous greater element first
        stack = []

        for i, x in enumerate(nums):
            while stack and x >= nums[stack[-1]]:
                stack.pop()
            PGE[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack.clear() # decreasing stack
        # find NGE next greater element
        for i, x in enumerate(nums):
            while stack and x >= nums[stack[-1]]:
                k = stack.pop()
                NGE[k] = i
            stack.append(i)
        
        # minima
        PLE = [-1] * N
        NLE = [N] * N

        stack.clear()
        for i, x in enumerate(nums):
            while stack and x <= nums[stack[-1]]:
                stack.pop()
            PLE[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack.clear()
        for i, x in enumerate(nums):
            while stack and x <= nums[stack[-1]]:
                k = stack.pop()
                NLE[k] = i
            stack.append(i)
        
        total_max = 0
        total_min = 0
        for i, x in enumerate(nums):
            left_max = (i - PGE[i])
            right_max = (NGE[i] - i)
            left_min = (i - PLE[i])
            right_min = (NLE[i] - i)
            total_max += x * left_max * right_max
            total_min += x * left_min * right_min
        return total_max - total_min


            

