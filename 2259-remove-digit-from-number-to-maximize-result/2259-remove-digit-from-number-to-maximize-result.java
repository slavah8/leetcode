class Solution {
    public String removeDigit(String number, char digit) {
        int n = number.length();
        int removeIndex = -1;

        for (int i = 0; i < n; i++) {
            if (number.charAt(i) == digit) {
                removeIndex = i;
                if (i + 1 < n && number.charAt(i + 1) > number.charAt(i)) {
                    break;
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (i == removeIndex) {
                continue;
            }
            sb.append(number.charAt(i));
        }
        return sb.toString();
    }
}