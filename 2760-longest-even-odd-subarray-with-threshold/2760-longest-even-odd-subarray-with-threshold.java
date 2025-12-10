class Solution {
    public int longestAlternatingSubarray(int[] nums, int threshold) {
        int n = nums.length;

        int cur = 0;
        int best = 0;

        for (int i = 0; i < n; i++) {
            int x = nums[i];

            if (x > threshold) {
                cur = 0;
                continue;
            }

            if (cur == 0) {
                if (x % 2 == 0) {
                    cur = 1;
                } else {
                    cur = 0;
                }
            } else {
                int prev = nums[i - 1];
                if (prev % 2 != x % 2) {
                    cur++;
                } else {
                    cur = (x % 2 == 0) ? 1 : 0;
                }
            }
            best = Math.max(best, cur);
        }
        return best;
    }
}