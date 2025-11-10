# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        freq = defaultdict(int) # how many ancestors have this prefix
        freq[0] = 1 # prefix : count
        ans = 0
        def dfs(node, prefix):
            nonlocal ans
            if not node:
                return
            
            prefix += node.val
            ans += freq[prefix - target]
            freq[prefix] += 1

            dfs(node.left, prefix)
            dfs(node.right, prefix)
            
            freq[prefix] -= 1
            
            
        dfs(root, 0)
        return ans