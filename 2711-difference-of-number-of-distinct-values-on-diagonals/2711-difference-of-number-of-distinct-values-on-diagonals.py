class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        def calculate(r, c): # calculate left above and right below diags
            left_above = set()
            right_below = set()
            r0 = r
            c0 = c


            # calculate right below
            while r + 1 < rows and c + 1 < cols:
                r += 1
                c += 1
                right_below.add(grid[r][c])
            
            r = r0
            c = c0

            # calculate left above
            while r - 1 >= 0 and c - 1 >= 0:
                r -= 1
                c -= 1
                left_above.add(grid[r][c])
            
            return abs(len(left_above) - len(right_below))
        
        answer = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                answer[r][c] = calculate(r, c)
        
        return answer


