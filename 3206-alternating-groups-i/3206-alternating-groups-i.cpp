class Solution {
public:
    int numberOfAlternatingGroups(vector<int>& colors) {
        
        int n = (int)colors.size();
        vector<int> arr(2 * n);
        for (int i = 0; i < 2 * n; i++) {
            arr[i] = colors[i % n];
        }

        for (int x : arr) cout << x << " ";

        int ans = 0;
        for (int s = 1; s < n + 1; s++) {
            if (arr[s] != arr[s - 1] && arr[s] != arr[s + 1]) {
                ans++;
            }
        }
        return ans;
    }
};