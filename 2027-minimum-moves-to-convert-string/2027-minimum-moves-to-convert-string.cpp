class Solution {
public:
    int minimumMoves(string s) {
        int n = s.size();

        int i = 0;
        int moves = 0;
        while(i < n) {
            int j = i;
            int count = 0;
            bool changed = false;
            while (j < n && count < 3) {
                count++;
                if (s[j] == 'X') {
                    moves++;
                    for (int k = 0; k < 3; k++) {
                        if (j + k < n) {
                            s[j + k] = 'O';
                        }
                    }
                    changed = true;
                    break;
                } else {
                    j++;
                }
                
            } 
            i += 3;
        }
        return moves;
    }
};