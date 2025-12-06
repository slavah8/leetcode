class Solution {
    public int countBinarySubstrings(String s) {
        
        int n = s.length();

        int[] groups = new int[n];

        groups[0] = 1;
        int group_idx = 0;

        for (int i = 1; i < n; i++) {
            if (s.charAt(i) == s.charAt(i - 1)) {
                groups[group_idx]++;
            } else {
                group_idx++;
                groups[group_idx] = 1;
            }
        }
        int result = 0;
        for (int i = 0; i < group_idx; i++) {
            result += Math.min(groups[i], groups[i + 1]);
        }
        return result;
    }
}