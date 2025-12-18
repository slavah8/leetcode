class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        
        res = []
        rows = len(grid)
        cols = len(grid[0])
        alt = 1
        res.append(grid[0][0])
        alt = 0
        
        r = 0
        c = 0
        while r < rows:
            print('hi')
            # move right until end of row
            while c + 1 < cols:
                c += 1
                if alt == 1:
                    res.append(grid[r][c])
                    alt = 0
                else:
                    alt = 1
            
            # drop down
            if r + 1 < rows:
                r += 1
                if alt == 1:
                    res.append(grid[r][c])
                    alt = 0
                else:
                    alt = 1
            else:
                break
            
            # then traverse left
            while c - 1 >= 0:
                c -= 1
                if alt == 1:
                    res.append(grid[r][c])
                    alt = 0
                else:
                    alt = 1
            
            if r + 1 < rows:
                r += 1
                if alt == 1:
                    res.append(grid[r][c])
                    alt = 0
                else:
                    alt = 1
            else:
                break
        return res
        

            


