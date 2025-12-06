class Solution {
    public boolean checkIfPangram(String sentence) {
        boolean[] seen = new boolean[26];

        for (int i = 0; i < sentence.length(); i++) {
            char c = sentence.charAt(i);
            int idx = c - 'a';
            seen[idx] = true;
        }

        for (int i = 0; i < 26; i++) {
            if (!seen[i]) {
                return false;
            }
        }
        return true;
    }
}