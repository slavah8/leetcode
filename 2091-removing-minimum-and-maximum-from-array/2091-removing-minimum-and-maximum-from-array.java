class Solution {
    public int minimumDeletions(int[] nums) {
        int n = nums.length;

        int min_idx = 0, max_idx = 0;

        for (int i = 0; i < n; i++) {
            if (nums[i] < nums[min_idx]) {
                min_idx = i;
            }
            if (nums[i] > nums[max_idx]) {
                max_idx = i;
            }
        }

        int L = Math.min(min_idx, max_idx);
        int R = Math.max(min_idx, max_idx);

        // 3 options
        
        // delete from the left
        int op1 = R + 1;

        // delete from the right
        int op2 = n - L;

        // delete from left and right
        int op3 = (L + 1) + (n - R);

        return Math.min(op1, Math.min(op2, op3));
    }
}