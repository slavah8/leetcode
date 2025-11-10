# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = defaultdict(list)   # col -> list of (row, val)
        minc = maxc = 0

        q = deque([(root, 0, 0)])
        while q:
            node, r, c = q.popleft()
            if not node: 
                continue
            cols[c].append((r, node.val))
            minc = min(minc, c); maxc = max(maxc, c)
            q.append((node.left,  r+1, c-1))
            q.append((node.right, r+1, c+1))

        ans = []

        for c in range(minc, maxc + 1):
            bucket = cols[c]
            bucket.sort(key = lambda x: (x[0], x[1]))
            ans.append([v for _, v in bucket])
        return ans


            

