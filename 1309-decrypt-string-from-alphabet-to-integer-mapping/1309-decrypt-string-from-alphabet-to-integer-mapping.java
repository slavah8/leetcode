class Solution {
    public String freqAlphabets(String s) {
        int n = s.length();
        int i = n - 1;
        StringBuilder sb = new StringBuilder();

        while (i >= 0) {
            char c = s.charAt(i);
            if (c == '#') {
                int d2 = s.charAt(i - 1) - '0';
                int d1 = s.charAt(i - 2) - '0';
                int num = d1 * 10 + d2;

                char ch = (char) ('a' + num - 1);
                sb.append(ch);
                i -= 3;
            } else {
                int num = s.charAt(i) - '0';
                char ch = (char) ('a' + num - 1);
                sb.append(ch);
                i -= 1;
            }
        }
        return sb.reverse().toString();
    }
}