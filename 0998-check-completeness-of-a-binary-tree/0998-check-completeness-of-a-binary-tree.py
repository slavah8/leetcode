# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        queue = deque([root])
        depth = 0
        def dfs(node, curr_depth):
            nonlocal depth
            if not node:
                return
            if curr_depth > depth:
                depth = curr_depth
            dfs(node.left, curr_depth + 1)
            dfs(node.right, curr_depth + 1)
        
        dfs(root, 0)
            

        print(depth)

        h = 0
        while queue:
            level_len = len(queue)
            print(h)
            if h == depth:
                return True
            if level_len != 2 ** h:
                return False
            mark = False
            for _ in range(level_len):
                
                node = queue.popleft()
                if not node.left and node.right:
                    return False
                
                
                if node.left and mark:
                    return False
                if node.right and mark:
                    return False

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if node.left and not node.right:
                    mark = True
                if not node.left and not node.right:
                    mark = True
            h += 1
        return True
