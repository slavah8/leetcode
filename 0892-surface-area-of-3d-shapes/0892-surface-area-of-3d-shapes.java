class Solution {
    public int surfaceArea(int[][] grid) {
        
        int rows = grid.length;
        int cols = grid[0].length;
        int area = 0;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                int h = grid[r][c];

                if (h > 0) {
                    area += 2;

                    area += (4 * h);

                    if (r > 0) {
                        area -= (2 * Math.min(h, grid[r - 1][c]));
                    }
                    if (c > 0) {
                        area -= (2 * Math.min(h, grid[r][c - 1]));
                    }
                }
            }

        }
        return area;
    }
}