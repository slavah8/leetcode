class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        

        rows = len(picture)
        cols = len(picture[0])
        
        rows_count = defaultdict(int)
        cols_count = defaultdict(int)
        for r in range(rows):
            for c in range(cols):
                if picture[r][c] == 'B':
                    rows_count[r] += 1
                    cols_count[c] += 1
        print(rows_count)
        print(cols_count)

        total = 0
        for r in range(rows):
            for c in range(cols):
                if picture[r][c] == 'B': # cand
                    if rows_count[r] == 1 and cols_count[c] == 1:
                        total += 1
        return total




