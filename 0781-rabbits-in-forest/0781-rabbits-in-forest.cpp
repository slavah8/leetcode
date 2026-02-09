class Solution {
public:
    int numRabbits(vector<int>& answers) {
        
        unordered_map<int, int> freq;
        for (int x : answers) {
            freq[x]++;
        }

        int rabbits = 0;
        for (auto &[x, c] : freq) {
            int group_size = x + 1;
            int groups = ceil((double)c / group_size);
            rabbits += groups * group_size;
        }
        return rabbits;
    }
};