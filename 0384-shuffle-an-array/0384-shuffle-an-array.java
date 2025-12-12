class Solution {

    private final int[] original;
    private final Random rand = new Random();
    public Solution(int[] nums) {
        original = nums.clone();
    }
    
    public int[] reset() {
        return original.clone();
    }
    
    public int[] shuffle() {
        List<Integer> bag = new ArrayList<>();
        for (int x : original) {
            bag.add(x);
        }
        int[] res = new int[original.length];

        for (int i = 0; i < res.length; i++) {
            int j = rand.nextInt(bag.size());
            res[i] = bag.get(j);
            bag.remove(j);
        }
        return res;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.reset();
 * int[] param_2 = obj.shuffle();
 */