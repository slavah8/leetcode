class Solution {
    public int countBalls(int lowLimit, int highLimit) {
        int[] boxes = new int[46];
        int max = 0;
        for (int x = lowLimit; x <= highLimit; x++) {
            int box = sum_digits(x);
            boxes[box]++;
            if (boxes[box] > max) {
                max = boxes[box];
            }
        }
        return max;
    }

    private int sum_digits(int x) {
        int sum = 0;
        while (x > 0) {
            int digit = x % 10;
            sum = sum + digit;
            x = x / 10;
        }
        return sum;
    }
}