class Solution {
    public boolean buddyStrings(String s, String goal) {
        
        if (s.length() != goal.length()) {
            return false;
        }


        if (s.equals(goal)) {
            int[] freq = new int[26];

            for(int i = 0; i < s.length(); i++) {
                int idx = s.charAt(i) - 'a';
                freq[idx]++;
                if (freq[idx] >= 2) {
                    return true;
                }
            }
            return false;
        }
        int first = -1;
        int second = -1;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != goal.charAt(i)) {
                if (first == -1) {
                    first = i;
                } else if (second == -1) {
                    second = i;
                } else {
                    return false;
                }
            }
        }
        if (second == -1) {
            return false;
        }
        return s.charAt(first) == goal.charAt(second) && s.charAt(second) == goal.charAt(first);
    }
}