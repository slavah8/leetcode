# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        
        A = []

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            A.append(node.val)
            inorder(node.right)
        
        inorder(root)
        print(A)
        n = len(A)
        answer = []
        for x in queries:
            i = bisect.bisect_right(A, x) - 1
            j = bisect.bisect_left(A, x)
            if i >= 0:
                mn = A[i]
            else:
                mn = -1
            
            if j < n:
                mx = A[j]
            else:
                mx = -1
            answer.append((mn, mx))
        return answer
            

            
    
            

            





