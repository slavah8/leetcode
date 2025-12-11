class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        rows = len(mat)
        cols = len(mat[0])

        total = rows * cols
        res = []
        up = True
        r = 0
        c = 0
        for _ in range(total):
            res.append(mat[r][c])

            if up:
                nr = r - 1
                nc = c + 1
                if 0 <= nr < rows and 0 <= nc < cols:
                    r = nr
                    c = nc
                else:
                    if c + 1 < cols:
                        c = c + 1
                        
                    else:
                        r = r + 1
                    up = False
            else:
                # going down left
                nr = r + 1
                nc = c - 1
                if 0 <= nr < rows and 0 <= nc < cols:
                    r = nr
                    c = nc
                else:
                    # try going down
                    if r + 1 < rows:
                        r = r + 1
                    else:
                        c = c + 1
                    up = True
        return res

