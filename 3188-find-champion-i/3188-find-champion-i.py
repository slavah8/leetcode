class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        champion = None

        n = len(grid)
        best_count = None
        for i in range(n):
            count = 0
            for j in range(n):
                if i == j:
                    continue
                if grid[i][j] == 1:
                    count += 1
            if not best_count or count > best_count:
                best_count = count
                champion = i
        return champion
                