class Solution {
    public int sumOfUnique(int[] nums) {
        int[] freq = new int[101];

        for (int x : nums) {
            freq[x]++;
        }
        
        int sum = 0;
        for (int val = 1; val <= 100; val++) {
            if (freq[val] == 1) {
                sum += val;
            }
        }
        return sum;
    }
}