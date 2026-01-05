class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        negs = 0
        total = 0
        INF = 10 ** 10
        min_val = INF
        for row in matrix:
            for x in row:
                if x < 0:
                    negs += 1
                ax = abs(x)
                total += ax
                if ax < min_val:
                    min_val = ax
        
        if negs % 2 == 0:
            return total
        
        return total - 2 * min_val
                
