class Solution {
    public int mostWordsFound(String[] sentences) {
        int max = 0;

        for (String s : sentences) {
            String[] words =  s.split(" ");
            max = Math.max(max, words.length);
        }
        return max;
    }
}