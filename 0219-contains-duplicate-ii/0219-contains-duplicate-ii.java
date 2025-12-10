class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> lastIndex = new HashMap<>();

        for (int r = 0; r < nums.length; r++) {
            int val = nums[r];

            if (lastIndex.containsKey(val)) {
                int l = lastIndex.get(val);
                if (r - l <= k) {
                    return true;
                }
            }
            lastIndex.put(val, r);
        }

        return false;
    }
}