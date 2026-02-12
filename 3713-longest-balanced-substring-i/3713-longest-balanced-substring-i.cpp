class Solution {
public:
    int longestBalanced(string s) {
        int n = (int)s.size();
        int best = 0;

        for (int i = 0; i < n; i++) {
            std::array<int, 26> counts{};
            counts.fill(0);

            for (int j = i; j < n; j++) {
                counts[s[j] - 'a']++;

                int target = 0;
                bool ok = true;
                for (int k = 0; k < 26; k++) {
                    if (counts[k] == 0) continue;
                    if (target == 0) target = counts[k];
                    else if (counts[k] != target) {
                        ok = false;
                        break;
                    }
                }
            
            if (ok) best = max(best, j - i + 1);
            }

        }
        return best;
    }
};