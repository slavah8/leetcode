class Solution {
    public int maxScore(int[] cardPoints, int k) {
        
        int n = cardPoints.length;
        int total = 0;

        for (int x : cardPoints) {
            total += x;
        }

        int length = n - k;

        if (length == 0) {
            return total;
        }

        int windowSum = 0;
        for (int r = 0; r < length; r++) {
            windowSum += cardPoints[r];
        }

        int minWindowSum = windowSum;
        int l = 0;
        for (int r = length; r < n; r++) {
            windowSum += cardPoints[r];

            windowSum -= cardPoints[l];
            l++;

            if (windowSum < minWindowSum) {
                minWindowSum = windowSum;
            }
            
        }

        return total - minWindowSum;
    }
}