class Solution {
    public boolean areOccurrencesEqual(String s) {
        Map<Character, Integer> freq = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }

        Set<Integer> seen = new HashSet<>();
        
        for (int v : freq.values()) {
            seen.add(v);
        }
        return seen.size() == 1;
    }
}