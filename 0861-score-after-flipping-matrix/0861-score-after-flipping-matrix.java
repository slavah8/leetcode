class Solution {
    public int matrixScore(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;

        for (int r = 0; r < rows; r++) {
            if (grid[r][0] == 0) {
                for (int c = 0; c < cols; c++) {
                    grid[r][c] ^= 1;
                }
            }
        }

        int score = 0;

        for (int c = 0; c < cols; c++) {
            int ones = 0;
            for (int r = 0; r < rows; r++) {
                if (grid[r][c] == 1) {
                    ones++;
                }
            }
            int zeros = rows - ones;
            if (zeros > ones) {
                for (int r = 0; r < rows; r++) {
                    grid[r][c] ^= 1;
                }
            }
        }

        int total = 0;
        for (int r = 0; r < rows; r++) {
            int row_sum = 0;
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 1) {
                    row_sum += (1 << (cols - c - 1));
                }
            }
            total += row_sum;
        }
        return total;
    }
}