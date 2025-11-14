# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        
        def push_left(node, stack):
            while node:
                stack.append(node)
                node = node.left
        
        stack1, stack2 = [], []
        push_left(root1, stack1)
        push_left(root2, stack2)

        res = []
        while stack1 or stack2:
            if not stack2 or (stack1 and stack1[-1].val <= stack2[-1].val):
                node = stack1.pop()
                res.append(node.val)
                push_left(node.right, stack1)
                
            else:
                node = stack2.pop()
                res.append(node.val)
                push_left(node.right, stack2)
        return res
