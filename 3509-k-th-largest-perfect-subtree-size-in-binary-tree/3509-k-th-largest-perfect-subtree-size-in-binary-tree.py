# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        sizes = []
        # return (leaf depth, # of nodes)
        def dfs(node):
            nonlocal sizes
            if not node:
                return (0, 0)
            
            
            left_count, left_depth = dfs(node.left)
            right_count, right_depth = dfs(node.right)
            subtree_size = left_count + right_count + 1
            # need min leaf depth and max leaf depth and check if they are equal

            if left_depth >= 0 and right_depth >= 0 and left_depth == right_depth:
                sizes.append(subtree_size)
                return (subtree_size, left_depth + 1)
            else:
                return (0, -1)
               
        dfs(root)
        print(sizes)
        sizes = [-s for s in sizes]
        heapify(sizes)
        
        while k > 0 and sizes:
            x = heapq.heappop(sizes)
            k -= 1
            if k == 0:
                return -x
        
        print(k)
        print(sizes)
        if k > 0 and not sizes:
            return -1
        
        

        
        