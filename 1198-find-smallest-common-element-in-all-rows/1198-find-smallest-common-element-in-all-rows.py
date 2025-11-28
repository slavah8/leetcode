class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        INF = 10 ** 10
        smallest = INF
        freq = defaultdict(int)
        for r in range(rows):
            for c in range(cols):
                val = mat[r][c]
                freq[val] += 1
        
        print(freq)
        for val, cnt in freq.items():
            if cnt == rows:
                smallest = min(smallest, val)
        
        return smallest if smallest != INF else -1