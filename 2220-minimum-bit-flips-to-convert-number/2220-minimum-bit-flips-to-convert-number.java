class Solution {
    public int minBitFlips(int start, int goal) {
        int z = start ^ goal;
        int count = 0;
        while (z > 0) {
            count += (z & 1);
            z = (z >> 1);
        }
        return count;
    }
}