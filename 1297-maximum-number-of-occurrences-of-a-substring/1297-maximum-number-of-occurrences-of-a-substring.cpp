class Solution {
public:
    int maxFreq(string s, int maxLetters, int minSize, int maxSize) {
        
        int best = 0;
        int l = 0;
        unordered_map<string, int> count;
        unordered_map<char, int> char_count;
        string substring = "";

        for (int r = 0; r < s.size(); r++) {
            char c = s[r];
            substring += c;
            char_count[c]++;

            while (substring.size() > minSize) {
                char left_char = s[l];
                char_count[left_char]--;

                if (char_count[left_char] == 0) {
                    char_count.erase(left_char);
                }

                substring = substring.substr(1);
                l++;
            }

            if (substring.size() == minSize && char_count.size() <= maxLetters) {
                count[substring]++;
                best = max(best, count[substring]);
            }
        }
        return best;
    }
};