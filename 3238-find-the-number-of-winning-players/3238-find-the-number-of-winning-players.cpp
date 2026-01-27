class Solution {
public:
    int winningPlayerCount(int n, vector<vector<int>>& pick) {
        
        unordered_map<int, unordered_map<int, int>> freq;

        for (auto &p : pick) {
            int player = p[0];
            int color = p[1];
            freq[player][color]++;
        }

        int winners = 0;

        for (int i = 0; i < n; i++) {
            bool win = false;

            if (freq.find(i) != freq.end()) {
                for (auto &kv : freq[i]) {
                    int cnt = kv.second;
                    if (cnt > i) {
                        win = true;
                        break;
                    }
                }
            }
            if (win) winners++;
        }
        return winners;
    }
};