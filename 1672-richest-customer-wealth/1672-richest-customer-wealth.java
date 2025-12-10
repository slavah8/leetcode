class Solution {
    public int maximumWealth(int[][] accounts) {
        int maxWealth = 0;

        for (int r = 0; r < accounts.length; r++) {
            int curWealth = 0;
            for (int c = 0; c < accounts[r].length; c++) {
                curWealth += accounts[r][c];
            }

            if (curWealth > maxWealth) {
                maxWealth = curWealth;
            }
        }
        return maxWealth;
    }
}