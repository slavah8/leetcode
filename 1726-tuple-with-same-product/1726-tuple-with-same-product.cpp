class Solution {
public:
    int tupleSameProduct(vector<int>& nums) {
        
        unordered_map<int, int> counts; // product -> number of pairs
        int n = (int)nums.size();

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int prod = nums[i] * nums[j];
                counts[prod]++;
            }
        }

        long long ans = 0;
        for (auto &kv : counts) {
            long long cnt = kv.second;
            ans += 8LL * (cnt * (cnt - 1) / 2);
        }
        return (int)ans;
    }
};