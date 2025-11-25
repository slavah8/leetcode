# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        sum_freq = defaultdict(int)

        def dfs(node):
            nonlocal sum_freq
            if not node:
                return 0 
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            subtree_sum = left_sum + right_sum + node.val
            sum_freq[subtree_sum] += 1
            return subtree_sum
            
        
        dfs(root)
        print(sum_freq)
        INF = 10 ** 10
        most_freq = 0
        ans = [0]
        for summ, frq in sum_freq.items():
            if frq > most_freq:
                most_freq = frq
                ans = [summ]
            elif frq == most_freq:
                ans.append(summ)
        return ans

