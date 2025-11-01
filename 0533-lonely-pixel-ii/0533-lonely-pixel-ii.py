class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        
        row_count = defaultdict(int)
        col_count = defaultdict(int)

        rows = len(picture)
        cols = len(picture[0])
        row_patterns = defaultdict(int)

        for r in range(rows):
            row_pattern = ''
            for c in range(cols):
                row_pattern += picture[r][c]
                if picture[r][c] == 'B':
                    row_count[r] += 1
                    col_count[c] += 1
            print(row_pattern)
            row_patterns[row_pattern] += 1
        total = 0
        print(row_patterns)
        for r in range(rows):
            pattern = ''
            ok = False
            count = 0
            for c in range(cols):
                pattern += picture[r][c]
                if picture[r][c] == 'B': # cand
                    if row_count[r] == target and col_count[c] == target:
                        count += 1
                        ok = True
            if ok and row_patterns[pattern] == target:
                total += count
        return total

             