class Solution {
    public String replaceDigits(String s) {
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            if (i % 2 == 1) {
                char prev = s.charAt(i - 1);
                int x = s.charAt(i) - '0';
                sb.append(shift(prev, x));
            } else {
                sb.append(s.charAt(i));
            }

        }
        return sb.toString();
    }
    private char shift(char c, int x) {
        return (char) (c + x);
    }
}