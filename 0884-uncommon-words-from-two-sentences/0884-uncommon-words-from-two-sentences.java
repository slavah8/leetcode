class Solution {
    public String[] uncommonFromSentences(String s1, String s2) {
        
        Map<String, Integer> freq = new HashMap<>();

        addWords(s1, freq);
        addWords(s2, freq);

        List<String> result = new ArrayList<>();
        for (String word : freq.keySet()) {
            if (freq.get(word) == 1) {
                result.add(word);
            }
        }
        return result.toArray(new String[0]);
    }

    public void addWords(String sentence, Map<String, Integer> freq) {
        String[] words = sentence.split(" ");
        for (String w: words) {
            freq.put(w, freq.getOrDefault(w, 0) + 1);

        }
    }
}