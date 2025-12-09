class Solution {
    public int countEven(int num) {
        int count = 0;
        for (int x = 1; x <= num; x++) {
            if (digit_sum(x) % 2 == 0) {
                count++;
            }
        }
        return count;
    }
    private int digit_sum(int x) {
        int sum = 0;
        while (x > 0) {
            int digit = x % 10;
            sum += digit;
            x /= 10;
        }
        return sum;

    }
}