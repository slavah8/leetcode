class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        stack = []

        for i, x in enumerate(heights):
            while stack and x >= heights[stack[-1]]:
                stack.pop()
            stack.append(i)
        
        return stack 