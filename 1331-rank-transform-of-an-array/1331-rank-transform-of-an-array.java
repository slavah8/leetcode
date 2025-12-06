class Solution {
    public int[] arrayRankTransform(int[] arr) {
        int n = arr.length;

        int[] sorted = arr.clone();
        Arrays.sort(sorted);

        Map<Integer, Integer> value_to_rank = new HashMap<>();
        int rank = 1;
        for (int x : sorted) {
            if (!value_to_rank.containsKey(x)) {
                value_to_rank.put(x, rank);
                rank++;
            }
        }

        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            result[i] = value_to_rank.get(arr[i]);
        }
        return result;
    }
}