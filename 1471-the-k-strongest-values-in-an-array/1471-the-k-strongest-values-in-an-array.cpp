class Solution {
public:
    vector<int> getStrongest(vector<int>& arr, int k) {
        

        int n = arr.size();
        vector<int> s = arr;
        sort(s.begin(), s.end());
        int center = (n - 1) / 2;

        int m = s[center];

        sort(s.begin(), s.end(), [&](int a, int b) {
            int da = abs(a - m);
            int db = abs(b - m);

            if (da != db) return da > db;

            return a > b;
        });

        s.resize(k);

        return s;

    }
};