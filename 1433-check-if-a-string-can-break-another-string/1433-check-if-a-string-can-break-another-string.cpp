class Solution {
public:
    bool checkIfCanBreak(string s1, string s2) {
        int n = s1.size();

        std::sort(s1.begin(), s1.end());
        std::sort(s2.begin(), s2.end());
        bool ok = true;
        for (int i = 0; i < n; i++) {
            if (s1[i] < s2[i]) {
                ok = false;
                break;
            } 
        }
        bool ok2 = true;
        for (int i = 0; i < n; i++) {
            if (s2[i] < s1[i]) {
                ok2 = false;
                break;
            }
        }
        return ok || ok2;
    }
};