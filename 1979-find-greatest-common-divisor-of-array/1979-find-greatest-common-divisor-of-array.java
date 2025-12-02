class Solution {
    public int findGCD(int[] nums) {
        int min = 1000;
        int max = 1;

        for (int x : nums) {
            if (x < min) {
                min = x;
            }
            if (x > max) {
                max = x;
            }
        }

        return gcd(min, max);
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = a % b;
            a = b;
            b = temp;
        }
        return a;

    }
}