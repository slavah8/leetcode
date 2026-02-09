class Solution {
public:
    vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
        unordered_map<int, vector<int>> buckets; 
        vector<vector<int>> res;

        for (int id = 0; id < (int)groupSizes.size(); id++) {
            int group_size = groupSizes[id];

            buckets[group_size].push_back(id);

            if ((int)buckets[group_size].size() == group_size) {
                res.push_back(buckets[group_size]);
                buckets[group_size].clear();
            }
        }

        return res;
    }
};