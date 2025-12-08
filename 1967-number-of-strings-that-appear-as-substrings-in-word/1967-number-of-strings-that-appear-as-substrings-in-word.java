class Solution {
    public int numOfStrings(String[] patterns, String word) {
        Set<String> substrings = new HashSet<>();

        int n = word.length();

        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                String sub = word.substring(i, j + 1);
                substrings.add(sub);
            }
        }

        int count = 0;
        for (String p : patterns) {
            if (substrings.contains(p)) {
                count++;
            }
        }
        return count;
    }
}