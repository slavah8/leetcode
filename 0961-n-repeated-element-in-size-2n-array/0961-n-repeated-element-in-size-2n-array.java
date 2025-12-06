class Solution {
    public int repeatedNTimes(int[] nums) {
        Set<Integer> seen = new HashSet<>();

        for (int x : nums) {
            if (seen.contains(x)) {
                return x;
            }
            seen.add(x);
        }
        return -1;
    }
}