class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        
        n = len(tiles)
        tiles.sort(key = lambda x: x[0])
        best = 0
        j = 0
        fully_covered = 0
        for i in range(n):
            start = tiles[i][0]
            end = start + carpetLen - 1
            while j < n and tiles[j][1] <= end:
                fully_covered += tiles[j][1] - tiles[j][0] + 1
                j += 1
            
            cur = fully_covered
            if j < n and tiles[j][0] <= end:
                cur += end - tiles[j][0] + 1
            
            best = max(best, cur)

            fully_covered -= tiles[i][1] - tiles[i][0] + 1
        
        return best