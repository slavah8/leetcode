class Solution {
    public int countKDifference(int[] nums, int k) {
        int n = nums.length;
        int count = 0;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int diff = Math.abs(nums[i] - nums[j]);
                if (diff == k) {
                    count++;
                }
            }
        }
        return count;
    }
}