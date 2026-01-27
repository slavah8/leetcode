class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        int avail[26] = {0};
        for (char ch : chars) {
            avail[ch - 'a']++;
        }
        int sum = 0;
        for (auto &word : words) {
            if (can_form(word, avail)) {
                sum += (int)word.size();
            }
        }
        return sum;
    }

private:
    bool can_form(const string& word, const int avail[26]) {
        int need[26] = {0};

        for (char ch : word) {
            int idx = ch - 'a';
            need[idx]++;
            if (need[idx] > avail[idx]) {
                return false;
            }
        }
        return true;
    }
};