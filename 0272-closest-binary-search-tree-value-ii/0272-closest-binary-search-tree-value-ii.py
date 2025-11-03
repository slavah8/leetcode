# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        heap = [] # (dist, node.val)
        heapify(heap)
        INF = 10 ** 15
        best_diff = INF
        def dfs(node):
            if not node:
                return
            nonlocal heap, best_diff, k
            cand_diff = abs(node.val - target)
            heapq.heappush(heap, (cand_diff, node.val))
 
        
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        print(heap)
        ans = []
        while heap and k > 0:
            _, node = heapq.heappop(heap)
            ans.append(node)
            k -= 1
        return ans