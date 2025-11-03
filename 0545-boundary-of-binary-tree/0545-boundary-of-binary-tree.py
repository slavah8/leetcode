# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        
        boundary = []
        boundary.append(root.val)
        if not root.left and not root.right:
            return [root.val]

        # get left boundary
        # node.left in left boundary
        # if node.left doesnt exist then no left boundary
        left_boundary = []
        def get_left(node):
            nonlocal left_boundary
            if not node:
                return

            if not node.left and not node.right: # leaf
                return
            
            left_boundary.append(node.val)

            if node.left:
                get_left(node.left)
            if not node.left and node.right:
                get_left(node.right)
                
        
        if not root.left:
            # no left boundary
            left_boundary = []
        else:
            get_left(root.left)
            boundary = boundary + left_boundary
        
        
        leaves = []
        def get_leaves(node):
            nonlocal leaves
            if not node:
                return
            
            if not node.left and not node.right: # leaf
                leaves.append(node.val)
                return
            
            get_leaves(node.left)
            get_leaves(node.right)

        
        get_leaves(root)
        boundary = boundary + leaves

        right_boundary = []
        def get_right(node):
            nonlocal right_boundary
            if not node:
                return
            
            if not node.left and not node.right:
                return
            
            right_boundary.append(node.val)
            if node.right:
                get_right(node.right)
            if not node.right and node.left:
                get_right(node.left)
           
        print(boundary)
        if not root.right:
            right_boundary = []
        else:
            get_right(root.right)
            right_boundary.reverse()
            boundary = boundary + right_boundary
        
        return boundary

