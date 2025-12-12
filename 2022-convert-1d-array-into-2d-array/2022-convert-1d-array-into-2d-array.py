class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        size = len(original)

        if m * n != size:
            return []
        
        new = [[0] * n for _ in range(m)]

        values = original
        i = 0
        r = 0
        c = 0
        rows = m
        cols = n

        while i < len(values):
            val = values[i]
            new[r][c] = val
            if r == rows - 1 and c == cols - 1:
                break
            if c == cols - 1:
                # next row
                r += 1
                c = 0
            else:
                c += 1
            
            i += 1
        return new


        
            


