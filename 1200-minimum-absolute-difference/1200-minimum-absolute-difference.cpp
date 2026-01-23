class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        

        sort(arr.begin(), arr.end());

        int best = INT_MAX;
        vector<vector<int>> ans;

        for (int i = 1; i < (int)arr.size(); i++) {
            best = min(best, arr[i] - arr[i - 1]);
        }

        for (int i = 1; i < (int)arr.size(); i++) {
            if (arr[i] - arr[i - 1] == best) {
                ans.push_back({arr[i - 1], arr[i]});
            }
        }
        return ans;
    }
};