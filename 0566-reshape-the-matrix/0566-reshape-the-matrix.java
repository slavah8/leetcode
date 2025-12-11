class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        int rows = mat.length;
        int cols = mat[0].length;

        if (rows * cols != r * c) {
            return mat;
        }

        int[][] res = new int[r][c];

        for (int k = 0; k < rows * cols; k++) {
            int oldRow = k / cols;
            int oldCol = k % cols;

            int newRow = k / c;
            int newCol = k % c;

            res[newRow][newCol] = mat[oldRow][oldCol];
        }
        return res;
    }
}