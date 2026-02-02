class Solution {
public:
    int getMaximumConsecutive(vector<int>& coins) {
        sort(coins.begin(), coins.end());

        long long reach = 0;

        for (int c : coins) {
            if (c > reach + 1) break;
            reach += c;
        }

        return reach + 1;
    }
};