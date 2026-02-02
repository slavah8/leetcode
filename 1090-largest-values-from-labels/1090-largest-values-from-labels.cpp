class Solution {
public:
    int largestValsFromLabels(vector<int>& values, vector<int>& labels, int numWanted, int useLimit) {
        int n = (int)values.size();

        // pair as (value, label)
        vector<pair<int, int>> items;
        
        for (int i = 0; i < n; i++) {
            items.push_back({values[i], labels[i]});
        }

        sort(items.begin(), items.end(), [](const auto& a, const auto& b) {
            return a.first > b.first;
        });

        unordered_map<int, int> used;
        long long sum = 0;
        int picked = 0;

        for (auto &it : items) {
            if (picked == numWanted) break;

            int val = it.first;
            int lab = it.second;

            if (used[lab] < useLimit) {
                used[lab]++;
                sum += val;
                picked++;
            }
        }
        return (int)sum;
    }
};