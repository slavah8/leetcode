class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        
        stack = []
        for i, char in enumerate(s):
            if stack and char != stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        
        return len(stack)