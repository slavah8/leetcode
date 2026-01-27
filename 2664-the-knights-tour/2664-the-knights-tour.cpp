class Solution {
public:
    vector<vector<int>> tourOfKnight(int rows, int cols, int r, int c) {
        board.assign(rows, vector<int>(cols, -1));
        board[r][c] = 0;
        dfs(rows, cols, r, c, 0);
        return board;
    }

private:
    vector<vector<int>> board;

    const int dx[8] = {2, 2, 1, 1, -1, -1, -2, -2 };
    const int dy[8] = {1, -1, 2, -2, 2, -2, 1, -1};

    bool in_bounds(int x, int y, int rows, int cols) {
        return x >= 0 && x < rows && y >= 0 && y < cols;
    }

    bool dfs(int rows, int cols, int x, int y, int step) {
        if (step == rows * cols - 1) return true;

        for (int k = 0; k < 8; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];

            if (!in_bounds(nx, ny, rows, cols)) continue;
            if (board[nx][ny] != -1) continue; // already visited

            board[nx][ny] = step + 1;
            if (dfs(rows, cols, nx, ny, step + 1)) return true;
            board[nx][ny] = -1;
        }

        return false;
    }

};