class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        

        rows = len(matrix)
        cols = len(matrix[0])

        transpose = [[0] * (rows) for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):
                print(r, c)
                transpose[c][r] = matrix[r][c]
        return transpose


        # 1 2 3
        # 4 5 6

        """
        1 4
        2 5
        3 6
        """