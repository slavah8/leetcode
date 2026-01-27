class Solution {
public:
    vector<vector<int>> queensAttacktheKing(vector<vector<int>>& queens, vector<int>& king) {
        
        bool has_queen[8][8] = {};
        for (auto &q : queens) {
            has_queen[q[0]][q[1]] = true;
        }

        // 8 directions: N, S, E, W, NE, NW, SE, SW
        int dx[8] = {-1,  1,  0,  0, -1, -1,  1,  1};
        int dy[8] = { 0,  0,  1, -1,  1, -1,  1, -1};

        vector<vector<int>> ans;
        for (int dir = 0; dir < 8; dir++) {
            int x = king[0] + dx[dir];
            int y = king[1] + dy[dir];

            while (x >= 0 && x < 8 && y >= 0 && y < 8) {
                if (has_queen[x][y]) {
                    ans.push_back({x, y});
                    break;
                }
                x += dx[dir];
                y += dy[dir];
            }

        }
        return ans;
    }
};