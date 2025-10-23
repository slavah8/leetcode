class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        res = [[0] * n for _ in range(m)]

        for i in range(m): # rows of first
            for j in range(n): # cols of second
                total = 0
                for t in range(k): # rows of second
                    total += (mat1[i][t] * mat2[t][j])
                res[i][j] = total
        return res


