class Solution {
    public String capitalizeTitle(String title) {
        String[] words = title.split(" ");

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < words.length; i++) {

            String w = words[i];
            String transformed;

            if (w.length() <= 2) {
                transformed = w.toLowerCase();
            } else {
                String first = w.substring(0, 1).toUpperCase();
                String rest = w.substring(1).toLowerCase();
                transformed = first + rest;
            }

            sb.append(transformed);
            // space if not last
            if (i != words.length - 1) {
                sb.append(" ");
            }
            
        }
        return sb.toString();
    }
}