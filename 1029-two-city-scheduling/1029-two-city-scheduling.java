class Solution {
    public int twoCitySchedCost(int[][] costs) {
        int n = costs.length / 2;

        Arrays.sort(costs, (p1, p2) -> (p1[0] - p2[0]) - (p1[1] - p2[1]));

        int total = 0;

        for (int i = 0; i < n; i++) {
            total += costs[i][0];
        }

        for (int i = n; i < 2 * n; i++) {
            total += costs[i][1];
        }
        return total;
    }
}