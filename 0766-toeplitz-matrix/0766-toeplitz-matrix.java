class Solution {
    public boolean isToeplitzMatrix(int[][] matrix) {
        
        int rows = matrix.length;
        int cols = matrix[0].length;

        for (int start_col = 0; start_col < cols; start_col++) {
            int val = matrix[0][start_col];
            int r = 1;
            int c = start_col + 1;
            while (r < rows && c < cols) {
                if (val != matrix[r][c]) {
                    return false;
                }
                r++;
                c++;
            }
        }

        for (int start_row = 1; start_row < rows; start_row++) {
            int val2 = matrix[start_row][0];
            int r = start_row + 1;
            int c = 1;
            while (r < rows && c < cols) {
                if (val2 != matrix[r][c]) {
                    return false;
                }
                r++;
                c++;
            }
        }
        return true;
    }
}