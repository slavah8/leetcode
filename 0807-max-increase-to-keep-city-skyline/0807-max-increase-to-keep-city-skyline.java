class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;

        int[] rowMax = new int[rows];
        int[] colMax = new int[cols];

        for (int r = 0; r < rows; r++) {
            int maxVal = 0;
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] > maxVal) {
                    maxVal = grid[r][c];
                }
            }
            rowMax[r] = maxVal;
        }

        for (int c = 0; c < cols; c++) {
            int maxVal = 0;
            for (int r = 0; r < rows; r++) {
                if (grid[r][c] > maxVal) {
                    maxVal = grid[r][c];
                }
            }
            colMax[c] = maxVal;
        }

        int diff = 0;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                int allowedHeight = Math.min(rowMax[r], colMax[c]);
                diff += (allowedHeight - grid[r][c]);
            }
        }
        return diff;
    }
}