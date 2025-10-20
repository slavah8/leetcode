class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        
        # L[i] = index of the Previous Greater Element (PGE) to the left of i
        # R[i] = index of the Next Greater Element (NGE) to the right of i

        N = len(nums) 
        L = [-1] * N
        R = [N] * N
        stack = [] # strictly decreasing stack
        for i, x in enumerate(nums):
            while stack and x > nums[stack[-1]]: # this number is NGE of popped index
                k = stack.pop()
                R[k] = i
            L[i] = stack[-1] if stack else -1
            stack.append(i)
        
        print(L)
        print(R)
        result = []
        for i in range(N):
            result.append(R[i] - L[i] - 1)
        return result


