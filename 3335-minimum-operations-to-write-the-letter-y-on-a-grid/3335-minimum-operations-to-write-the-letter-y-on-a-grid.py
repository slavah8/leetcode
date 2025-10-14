class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        N = len(grid)

        mid = N // 2

        # counts of Y and not-Y for values 0,1,2

        countY = [0,0,0]
        countN = [0,0,0]

        for r in range(N):
            for c in range(N):

                val = grid[r][c]

                in_left_diag = (r == c) and (r <= mid)
                in_right_diag = (r + c == N - 1) and (r <= mid)
                in_vertical = (r >= mid) and (c == mid)

                if in_left_diag or in_right_diag or in_vertical:
                    countY[val] += 1
                else:
                    countN[val] += 1
        
        totalY = sum(countY)
        totalN = sum(countN)

        INF = 10 ** 10
        best = INF

        for a in (0, 1, 2): # value to set Y
            costY = totalY - countY[a]
            for b in (0, 1, 2):
                if a == b:
                    continue
                costN = totalN - countN[b]
                best = min(best, costY + costN)
        return best
