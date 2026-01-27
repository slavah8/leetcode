class Solution {
public:
    int numberOfAlternatingGroups(vector<int>& colors, int k) {
        int n = (int)colors.size();

        vector<int> arr(2 * n);
        for (int i = 0; i < 2 * n; i++) {
            arr[i] = colors[i % n];
        }

        vector<int> streak(2 * n, 1);
        for (int i = 1; i < 2 * n; i++) {
            if (arr[i] != arr[i - 1]) streak[i] = streak[i - 1] + 1;
            else streak[i] = 1;
        }

        int ans = 0;

        for (int s = 0; s < n; s++) {
            int end = s + k - 1;
            if (end < 2 * n && streak[end] >= k) {
                ans++;
            }
        }
        return ans;
    }

};