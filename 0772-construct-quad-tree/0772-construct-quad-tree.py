"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
         
        def is_uniform(r0, c0, size):
            val = grid[r0][c0]
            for r in range(r0, r0 + size):
                for c in range(c0, c0 + size):
                    if grid[r][c] != val:
                        return False, None
            return True, val
        
        def build(r0, c0, size):
            ok, val = is_uniform(r0, c0, size)
            if ok:
                return Node(bool(val), True, None, None, None, None)
            half = size // 2
            tl = build(r0, c0, half)
            tr = build(r0, c0 + half, half)
            bl = build(r0 + half, c0, half)
            br = build(r0 + half, c0 + half, half)
            return Node(True, False, tl, tr, bl, br)
        
        return build(0, 0, n)
            
        

            


        