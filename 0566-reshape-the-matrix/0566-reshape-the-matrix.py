class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        new_mat = [[0] * c for _ in range(r)]
        
        rows = len(mat)
        cols = len(mat[0])
        values = []

        for row in range(rows):
            for col in range(cols):
                values.append(mat[row][col])
        
        if len(values) != r * c:
            return mat

        i = 0
        nr = 0
        nc = 0
        while i < len(values):
            new_mat[nr][nc] = values[i]
            i += 1
            nc += 1
            if nc == c:
                nr += 1
                nc = 0
    
        return new_mat
            

            
