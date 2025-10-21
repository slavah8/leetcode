class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        stack1 = [] # hasnt seen it's first greater yet
        stack2 = [] # has seen it's first greater, waiting for second
        buf = []
        N = len(nums)
        ans = [-1] * N

        for i, x in enumerate(nums):
            # stack2 first
            while stack2 and x > nums[stack2[-1]]:
                k = stack2.pop()
                ans[k] = x
            
            
            while stack1 and x > nums[stack1[-1]]:
                buf.append(stack1.pop())
            while buf:
                stack2.append(buf.pop())


            stack1.append(i)
        return ans
        


