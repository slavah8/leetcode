class Solution {
    bool inside(int px, int py, int x, int y, int r) {
            int dx = px - x;
            int dy = py - y;

            return dx * dx + dy * dy <= r * r;
        }
public:
    vector<int> countPoints(vector<vector<int>>& points, vector<vector<int>>& queries) {
        vector<int> answer;

        

        for (auto &q : queries) {
            int x = q[0];
            int y = q[1];
            int r = q[2];

            int cnt = 0;
            for (auto &p : points) {
                if (inside(p[0], p[1], x, y, r)) {
                    cnt++;
                }
            }
            answer.push_back(cnt);
        }
        return answer;
    }
};