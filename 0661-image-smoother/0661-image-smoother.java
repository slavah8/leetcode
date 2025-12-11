class Solution {
    public int[][] imageSmoother(int[][] img) {
        int rows = img.length;
        int cols = img[0].length;

        int[][] res = new int[rows][cols];
        int[] directions = {-1, 0, 1};

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                int total = 0;
                int count = 0;

                for (int dr : directions) {
                    for (int dc : directions) {
                        int nr = dr + r;
                        int nc = dc + c;
                        if (nr >= 0 && nr < rows && nc >= 0 && nc < cols) {
                            total += img[nr][nc];
                            count++;
                        } 
                    }
                }
                res[r][c] = total / count;
            }
        }
        return res;
    }
}