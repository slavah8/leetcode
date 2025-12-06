class Solution {
    public int[] numberOfLines(int[] widths, String s) {
        int pixels = 100;
        int lines = 1;
        int curr_line = 0;
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            int idx = c - 'a';
            int width = widths[idx];
            if (pixels - width >= 0) {
                pixels -= width;
                curr_line += width;
            } else {
                lines++;
                pixels = 100 - width;
                curr_line = width;
            }
        }
        System.out.println(lines);
        System.out.println(curr_line);
        int[] result = new int[2];
        result[0] = lines;
        result[1] = curr_line;
        return result;
        
    }
}