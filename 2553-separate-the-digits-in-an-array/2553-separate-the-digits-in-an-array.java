class Solution {
    public int[] separateDigits(int[] nums) {
        List<Integer> digits = new ArrayList<>();

        for (int num : nums) {
            String s = String.valueOf(num);

            for (int i = 0; i < s.length(); i++) {
                char c = s.charAt(i);

                int digit = c - '0';

                digits.add(digit);
            }
        }
        int[] answer = new int[digits.size()];
        for (int i = 0; i < digits.size(); i++) {
            answer[i] = digits.get(i);
        }
        return answer;
    }
}