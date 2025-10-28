class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        rows = len(seats)
        cols = len(seats[0])

        # # Build a "broken mask" per row: bit j = 1 means seat j is broken ('#')
        broken = []
        for r in range(rows):
            mask = 0
            for c in range(cols):
                if seats[r][c] == '#': # broken
                    mask |= (1 << c)
            broken.append(mask)
        
        # Precompute valid masks for each row:
        valid = []
        for r in range(rows):
            row_valid = []
            for mask in range(1 << cols):
                if (mask & broken[r]) != 0: # check for broken seats
                    continue
                
                if (mask & (mask << 1)) != 0: # check for adjacent students
                    continue 

                row_valid.append(mask)
            valid.append(row_valid)

        # DP[r][cur] = max number of students you can seat from rows 0..r if row r uses mask = cur
        dp = {}

        for cur in valid[0]:
            dp[cur] = cur.bit_count()
        
        for r in range(1, rows):
            new_dp = {}
            for cur in valid[r]:
                best = 0
                for prev, val in dp.items():
                    if ((cur << 1) & prev) == 0 and ((cur >> 1) & prev) == 0:
                        best = max(best, val + cur.bit_count())
                new_dp[cur] = best
            dp = new_dp
        return max(dp.values())

