class Solution {
    public int minimumCardPickup(int[] cards) {
        Map<Integer, Integer> lastIndex = new HashMap<>();
        int n = cards.length;
        int best = Integer.MAX_VALUE;

        for (int i = 0; i < n; i++) {
            int val = cards[i];

            if (lastIndex.containsKey(val)) {
                int cand = i - lastIndex.get(val) + 1;
                best = Math.min(cand, best);
            }
            lastIndex.put(val, i);
        }

        return best == Integer.MAX_VALUE ? -1 : best;
    }
}