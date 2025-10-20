class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        INF = 10 ** 15
        lower_bound = -INF
        stack = []
        for x in preorder:
            if x < lower_bound:
                return False
            while stack and x > stack[-1]: # means we went right
                lower_bound = stack.pop()
            stack.append(x)
            
        return True