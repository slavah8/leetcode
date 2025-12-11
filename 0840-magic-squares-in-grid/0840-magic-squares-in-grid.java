class Solution {
    public int numMagicSquaresInside(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int count = 0;
        for (int r = 0; r <= rows - 3; r++) {
            for (int c = 0; c <= cols - 3; c++) {
                if (isMagic(grid, r, c)) {
                    count++;
                }
            }
        }
        return count;
    }
    private boolean isMagic(int[][] grid, int r0, int c0) {
        boolean[] seen = new boolean[10];

        for (int r = r0; r < r0 + 3; r++) {
            for (int c = c0; c < c0 + 3; c++) {
                int x = grid[r][c];
                if (x < 1 || x > 9) {
                    return false;
                }
                if (seen[x]) {
                    return false;
                }
                seen[x] = true;
            }
        }

        int target = grid[r0][c0] + grid[r0][c0 + 1] + grid[r0][c0 + 2];

        for (int dr = 0; dr < 3; dr++) {
            int rowSum = grid[r0 + dr][c0] + grid[r0 + dr][c0 + 1] + grid[r0 + dr][c0 + 2];
            if (rowSum != target){
                return false;
            }
        }

        for (int dc = 0; dc < 3; dc++) {
            int colSum = grid[r0][c0 + dc] + grid[r0 + 1][c0 + dc] + grid[r0 + 2][c0 + dc];
            if (colSum != target) {
                return false;
            }
        }

        int diag1 = grid[r0][c0] + grid[r0 + 1][c0 + 1] + grid[r0 + 2][c0 + 2];
        if (diag1 != target) {
            return false;
        }
        int diag2 = grid[r0 + 2][c0] + grid[r0 + 1][c0 + 1] + grid[r0][c0 + 2];
        if (diag2 != target) {
            return false;
        }
        return true;

    }
}