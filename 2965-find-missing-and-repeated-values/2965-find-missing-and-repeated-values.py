class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)

        values = [i for i in range(1, (n ** 2) + 1)]
        print(values)
        seen = set()
        b = None
        a = None
        for r in range(n):
            for c in range(n):
                x = grid[r][c]
                if x not in values:
                    b = x
                if x in seen:
                    a = x
                seen.add(x)

        for x in values:
            if x not in seen:
                b = x
            
        return [a, b]
                