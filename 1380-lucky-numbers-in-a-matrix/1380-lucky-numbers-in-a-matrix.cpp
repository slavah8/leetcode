class Solution {
public:
    vector<int> luckyNumbers(vector<vector<int>>& matrix) {
        
        int rows = matrix.size();
        int cols = matrix[0].size();

        vector<int> row_min(rows, INT_MAX);
        vector<int> col_max(cols, INT_MIN);

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                row_min[r] = min(row_min[r], matrix[r][c]);
            }
        }

        for (int c = 0; c < cols; c++) {
            for (int r = 0; r < rows; r++) {
                col_max[c] = max(col_max[c], matrix[r][c]);
            }
        }

        vector<int> res;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (matrix[r][c] == row_min[r] && matrix[r][c] == col_max[c]) {
                    res.push_back(matrix[r][c]);
                }
            }
        }
        return res;
    }
};