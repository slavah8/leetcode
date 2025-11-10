# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        freq = defaultdict(int)
        ans = []
        # post order traversal
        def dfs(node):
            if not node:
                return '#'
            
            left = dfs(node.left)
            right = dfs(node.right)
            sig = f"{node.val},{left},{right}"
            freq[sig] += 1
            if freq[sig] == 2:
                ans.append(node)
            return sig
        
        dfs(root)
        return ans
            
