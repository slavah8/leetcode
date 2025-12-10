class Solution {
    public int maximumLengthSubstring(String s) {
        
        Map<Character,Integer> count = new HashMap<>();
        int n = s.length();
        int l = 0;
        int best = 0;
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            count.put(c, count.getOrDefault(c, 0) + 1);

            while (l < n && count.get(c) > 2) {
                char c_left = s.charAt(l);
                count.put(c_left, count.get(c_left) - 1);
                l++;
            }

        best = Math.max(best, i - l + 1);
        }
        return best;
    }
}