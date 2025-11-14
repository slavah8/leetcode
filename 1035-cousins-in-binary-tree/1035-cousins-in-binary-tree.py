# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        parent_x = None
        depth_x = None
        parent_y = None
        depth_y = None
        def dfs(node, parent, depth):
            nonlocal parent_x, depth_x, parent_y, depth_y
            if not node:
                return
            
            if node.val == x:
                parent_x = parent
                depth_x = depth
            
            if node.val == y:
                parent_y = parent
                depth_y = depth
            dfs(node.left, node, depth + 1)
            dfs(node.right, node, depth + 1)
        
        
        dfs(root, -1, 0)
        print(parent_x)
        print(depth_x)
        if depth_x == depth_y and parent_x != parent_y:
            return True
        else:
            return False
