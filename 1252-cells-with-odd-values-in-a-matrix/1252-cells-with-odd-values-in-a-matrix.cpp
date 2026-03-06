class Solution {
public:
    int oddCells(int m, int n, vector<vector<int>>& indices) {
        
        vector<vector<int>> grid(m, vector<int>(n, 0));
        for (auto& idx : indices) {
            int row = idx[0];
            int col = idx[1];
            for (int r = 0; r < m; r++) {
                grid[r][col]++;
            }

            for (int c = 0; c < n; c++) {
                grid[row][c]++;
            }
            
        }

        int count = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] % 2 == 1) {
                    count++;
                }
            }
        }
        return count;
    }

};