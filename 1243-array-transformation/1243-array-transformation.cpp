class Solution {
public:
    vector<int> transformArray(vector<int>& arr) {
        int n = arr.size();
        vector<int> prev = arr;
        while (true) {
            vector<int> next = prev;
            bool changed = false;
            for (int i = 1; i < n - 1; i++) {
                if (prev[i] < prev[i - 1] && prev[i] < prev[i + 1]) {
                    changed = true;
                    next[i] = prev[i] + 1;
                }
                else if (prev[i] > prev[i - 1] && prev[i] > prev[i + 1]) {
                    next[i] = prev[i] - 1;
                    changed = true;
                }
            }
            if (!changed) {
                return prev;
            }
            prev = next;

        }
    }
};