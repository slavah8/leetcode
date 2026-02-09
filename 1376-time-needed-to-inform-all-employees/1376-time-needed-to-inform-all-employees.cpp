class Solution {
public:
    int numOfMinutes(int n, int headID, vector<int>& manager, vector<int>& informTime) {
        
        vector<vector<int>> subs(n);

        for (int i = 0; i < n; i++) {
            if (manager[i] != -1) {
                subs[manager[i]].push_back(i);
            }
        } 

        queue<pair<int, int>> q;
        q.push({headID, 0});

        int ans = 0;

        while (!q.empty()) {
            auto [u, t] = q.front();
            q.pop();

            ans = max(ans, t);

            for (int v : subs[u]) {
                q.push({v, t + informTime[u]});
            }
        }

        return ans;
    }
};