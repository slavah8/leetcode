class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        
        for _ in range(4):
            transpose = [[0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    transpose[c][r] = mat[r][c]
            
            for row in transpose:
                row.reverse()
            
            if transpose == target:
                return True
            
            mat = transpose[:]
        
        return False
        

