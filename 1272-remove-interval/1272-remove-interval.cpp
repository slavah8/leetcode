class Solution {
public:
    vector<vector<int>> removeInterval(vector<vector<int>>& intervals, vector<int>& toBeRemoved) {
        int l = toBeRemoved[0];
        int r = toBeRemoved[1];

        vector<vector<int>> res;

        for (auto& interval : intervals) {
            int a = interval[0];
            int b = interval[1];

            // no overlaps - > keep whole interval
            if (b <= l || a >= r) {
                res.push_back({a, b});
            }

            else {
                if (a < l) {
                    res.push_back({a, l});
                }

                if (b > r) {
                    res.push_back({r, b});
                }
            }
        }
        return res;
    }
};