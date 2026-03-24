class Solution {
public:
    vector<int> sumEvenAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
        
        vector<int> answer;
        for (auto &q : queries) {
            int val = q[0];
            int idx = q[1];

            nums[idx] += val;
            int sum = 0;
            for (auto &x : nums) {
                if (x % 2 == 0) {
                    sum += x;
                }
            }
            answer.push_back(sum);
        }
        
        return answer;
    }
};