# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        inorder = []
        def traverse(node):
            nonlocal inorder
            if not node:
                return None
            
            traverse(node.left)
            inorder.append(node.val)
            traverse(node.right)

        traverse(root)
        print(inorder)
        
        def build(low, high):
            if low > high:
                return None
            
            mid = (low + high) // 2
            root = TreeNode(inorder[mid])

            root.left = build(low, mid - 1)
            root.right = build(mid + 1, high)

            return root

            
        
        N = len(inorder)
        return build(0, N - 1)

            

