class Solution {
public:
    int maxNumberOfApples(vector<int>& weight) {
        sort(weight.begin(), weight.end());

        int apples = 0;
        int left = 5000;
        for (auto &w : weight) {
            if (w > left) break;
            apples++;
            left -= w;
        }
        return apples;
    }
};