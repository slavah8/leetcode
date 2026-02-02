class Solution {
public:
    int minPatches(vector<int>& nums, int n) {
        sort(nums.begin(), nums.end());
        long long reach = 0;
        int m = (int)nums.size();
        int patches = 0;
        int i = 0;

        while (reach < n) {
            if (i < m && nums[i] <= reach + 1) {
                reach += nums[i];
                i++;
            } else {
                    long long patch = reach + 1;
                    reach += patch;
                    patches++;
                }
            }
        return patches;
        }
        

};