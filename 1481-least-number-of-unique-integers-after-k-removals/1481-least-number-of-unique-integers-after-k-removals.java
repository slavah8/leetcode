class Solution {
    public int findLeastNumOfUniqueInts(int[] arr, int k) {
        Map<Integer, Integer> freq = new HashMap<>();

        for (int x : arr) {
            freq.put(x, freq.getOrDefault(x, 0) + 1);
        }

        List<Integer> counts = new ArrayList<>();
        for (int cnt : freq.values()) {
            counts.add(cnt);
        }

        Collections.sort(counts);

        int unique = counts.size();

        for (int f : counts) {
            if (f <= k) {
                k -= f;
                unique--;
            } else {
                break;
            }
        }
        return unique;
    }
}