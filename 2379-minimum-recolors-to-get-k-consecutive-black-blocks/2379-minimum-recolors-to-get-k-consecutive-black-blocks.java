class Solution {
    public int minimumRecolors(String blocks, int k) {
        int n = blocks.length();

        int blacks = 0;
        for (int i = 0; i < k; i++) {
            if (blocks.charAt(i) == 'B') {
                blacks++;
            }
        }
        int best = k - blacks;
        int l = 0;
        for (int r = k; r < n; r++) {
            if (blocks.charAt(r) == 'B') {
                blacks++;
            }
            if (blocks.charAt(l) == 'B') {
                blacks--;
            }
            l++;
            
            best = Math.min(best, k - blacks);
        }

        return best;
    }
}