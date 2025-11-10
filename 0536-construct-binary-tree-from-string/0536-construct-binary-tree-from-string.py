# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        n = len(s)
        i = 0
        def parse_int():
            nonlocal i
            sign = 1
            if i < n and s[i] == '-':
                sign = -1
                i += 1
            num = 0
            while i < n and s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
                i += 1
            return num * sign
            

        def parse_node():
            nonlocal i
            if i >= n:
                return None
            
            val = parse_int()
            node = TreeNode(val)

            if i < n and s[i] == '(':
                i += 1
                node.left = parse_node()
                i += 1
            
            if i < n and s[i] == '(':
                i += 1
                node.right = parse_node()
                i += 1
            return node
        return parse_node()
            
            
            