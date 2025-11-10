# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        sums = []
        def post(node):
            nonlocal sums
            if not node:
                return 0
            
            left_sum = post(node.left)
            right_sum = post(node.right)
            s = node.val + left_sum + right_sum
            sums.append(s)
            return s
        
        post(root)
        total = sums.pop()
        if total % 2 != 0:
            return False
        
        target = total // 2
        if target == 0:
            return 0 in sums
        return target in sums 



