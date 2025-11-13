# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        
        count = 0
        def dfs(node): # return True/False if uni value subtree and the value
            nonlocal count
            if not node:
                return True, None
            
            if not node.left and not node.right:
                count += 1
                return True, node.val
            


            is_uni_left, left_val = dfs(node.left)
            is_uni_right, right_val = dfs(node.right)
            if is_uni_left and is_uni_right and (left_val == right_val == node.val):
                count += 1
                return True, node.val
            elif is_uni_left and is_uni_right and left_val == node.val and right_val is None:
                count += 1
                return True, node.val
            elif is_uni_left and is_uni_right and right_val == node.val and left_val is None:
                count += 1
                return True, node.val
            # if not uni
            return False, None


        
        dfs(root)
        return count