class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        StringBuilder sb1 = new StringBuilder();
        StringBuilder sb2 = new StringBuilder();
        for (String w : word1) {
            for (int i = 0; i < w.length(); i++) {
                char c = w.charAt(i);
                sb1.append(c);
            }
        }

        for (String w2 : word2) {
            for (int j = 0; j < w2.length(); j++) {
                char c2 = w2.charAt(j);
                sb2.append(c2);
            }
        }
        String string1 = sb1.toString();
        String string2 = sb2.toString();
        return string1.equals(string2);
    }
}