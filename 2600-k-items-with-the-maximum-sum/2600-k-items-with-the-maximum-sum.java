class Solution {
    public int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
        int max = 0;
        while (k > 0) {
            if (numOnes > 0) {
                max++;
                numOnes--;
                k--;
                continue;
            }
            if (numOnes == 0 && numZeros > 0) {
                numZeros--;
                k--;
                continue;
            }
            if (numOnes == 0 && numZeros == 0 && numNegOnes > 0) {
                numNegOnes--;
                max--;
                k--;
                continue;
            }
        }
        return max;
    }
}