class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        
        rows = len(image)
        cols = len(image[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def is_region(r0, c0):
            start_r = r0
            start_c = c0

            for r in range(r0, r0 + 3):
                for c in range(c0, c0 + 3):
                    x = image[r][c]
                    
                    for dr, dc in directions:
                        nr, nc = dr + r, dc + c
                        if nr < r0 or nr >= r0 + 3 or nc < c0 or nc >= c0 + 3:
                            continue
                            
                        new_x = image[nr][nc]
                        diff = abs(x - new_x)
                        if diff > threshold:
                            return False
            return True
        

        new_grid = [[(0, 0)] * cols for _ in range(rows)]
        def add_region_avg(r0, c0):

            total = 0
            for r in range(r0, r0 + 3):
                for c in range(c0, c0 + 3):
                    x = image[r][c]
                    total += x

            avg = total // 9

            for r in range(r0, r0 + 3):
                for c in range(c0, c0 + 3):
                    s, cnt = new_grid[r][c]
                    new_grid[r][c] = (s + avg, cnt + 1)
        
        for start_r in range(0, rows - 3 + 1):
            for start_c in range(0, cols - 3 + 1):
                if is_region(start_r, start_c):
                    add_region_avg(start_r, start_c)

        result = [[0] * cols for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                s, cnt = new_grid[r][c]
                result[r][c] = s // cnt if cnt > 0 else image[r][c]
        
        return result


                    