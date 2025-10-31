class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        
        rows = len(matrix)
        cols = len(matrix[0])

        xor_matrix = [[0] * (cols + 1) for _ in range(rows + 1)]
        values = []
        for r in range(rows):
            prefix_xor = 0
            for c in range(cols):
                prefix_xor ^= matrix[r][c]
                above = xor_matrix[r][c + 1]
                xor_matrix[r + 1][c + 1] = prefix_xor ^ above
                values.append(-xor_matrix[r + 1][c + 1])
        
        heapify(values)
        print(values)
        x = 0
        while values and k > 0:
            x = heapq.heappop(values)
            k -= 1
        return -x
        