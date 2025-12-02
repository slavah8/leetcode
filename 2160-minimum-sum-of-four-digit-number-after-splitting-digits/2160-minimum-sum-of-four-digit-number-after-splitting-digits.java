class Solution {
    public int minimumSum(int num) {
        int[] d = new int[4];
        int i = 0;

        while (num > 0) {
            int digit = num % 10;
            d[i] = digit;
            num /= 10;
            i++;
        }
        Arrays.sort(d);

        int new1 = d[0] * 10 + d[2];
        int new2 = d[1] * 10 + d[3];
        return new1 + new2;
    }
}