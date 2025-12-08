class Solution {
    public String greatestLetter(String s) {
        boolean[] lower = new boolean[26];
        boolean[] upper = new boolean[26];

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (c >= 'a' && c <= 'z') {
                lower[c - 'a'] = true;
            } else {
                upper[c - 'A'] = true;
            }
        }

        for (int i = 25; i >= 0; i--) {
            if (lower[i] && upper[i]) {
                char letter = (char) (i + 'A');
                return String.valueOf(letter);
            }
        }
        return "";
    }

}