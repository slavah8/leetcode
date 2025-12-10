class Solution {
    public int divisorSubstrings(int num, int k) {
        String s = String.valueOf(num);
        int n = s.length();
        int count = 0;
        for (int i = 0; i + k <= n; i++) {
            String sub = s.substring(i, i + k);
            int val = Integer.parseInt(sub);

            if (val == 0) {
                continue;
            }
            
            if (num % val == 0) {
                count++;
            }
        }
        return count;
    }
}