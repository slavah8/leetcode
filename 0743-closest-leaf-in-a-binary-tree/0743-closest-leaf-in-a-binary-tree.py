# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        
        # we can find leaves
        # then we can bfs form the leaf and get the largest distance
        leaves = []
        def dfs(node):
            nonlocal leaves
            if not node:
                return
            
            if not node.left and not node.right:
                leaves.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        graph = defaultdict(list)
        def dfs2(node):
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                dfs2(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                dfs2(node.right)
        
        dfs2(root)


        def bfs(start):
            dist = {start : 0} # node : distance
            queue = deque([start])
            far = start
            while queue:
                node = queue.popleft()
                far = node
                for nei in graph[node]:
                    if nei not in dist:
                        dist[nei] = 1 + dist[node]
                        queue.append(nei)

            return far, dist
        
        node, dist = bfs(k) # dist from root to each node
        
        INF = 10 ** 10
        min_node = None
        min_dist = INF
        for leaf in leaves:
            cur_dist = dist[leaf]
            if not min_node or cur_dist < min_dist:
                min_node = leaf
                min_dist = cur_dist
        return min_node
        

