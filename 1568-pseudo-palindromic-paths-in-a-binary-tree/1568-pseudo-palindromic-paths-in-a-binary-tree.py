# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        freq = [0] * 10

        def dfs(node):
            nonlocal ans, freq
            if not node:
                return
            freq[node.val] += 1

            if not node.left and not node.right:
                odd = 0
                for x in freq:
                    if x % 2 == 1:
                        odd += 1
                if odd <= 1:
                    ans += 1
            
            dfs(node.left)
            dfs(node.right)
            freq[node.val] -= 1
        
        dfs(root)
        return ans


            
        
        dfs(root)
