class Solution {
    public int projectionArea(int[][] grid) {
        int n = grid.length;

        int front = 0;
        int side = 0;
        int top = 0;

        for (int r = 0; r < n; r++) {
            int rowMax = 0;

            for (int c = 0; c < n; c++) {
                int val = grid[r][c];

                if (val > 0) {
                    top++;
                }
                
                if (val > rowMax) {
                    rowMax = val;
                }
            }
            front += rowMax;
        }

        for (int c = 0; c < n; c++) {
            int colMax = 0;
            for (int r = 0; r < n; r++) {
                int val = grid[r][c];
                if (val > colMax) {
                    colMax = val;
                }

            }
            side += colMax;
        }
        return side + front + top;
    } 
}