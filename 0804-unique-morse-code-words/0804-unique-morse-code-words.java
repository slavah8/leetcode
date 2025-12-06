class Solution {
    public int uniqueMorseRepresentations(String[] words) {
        String[] morse = {
            ".-",   // a
            "-...", // b
            "-.-.", // c
            "-..",  // d
            ".",    // e
            "..-.", // f
            "--.",  // g
            "....", // h
            "..",   // i
            ".---", // j
            "-.-",  // k
            ".-..", // l
            "--",   // m
            "-.",   // n
            "---",  // o
            ".--.", // p
            "--.-", // q
            ".-.",  // r
            "...",  // s
            "-",    // t
            "..-",  // u
            "...-", // v
            ".--",  // w
            "-..-", // x
            "-.--", // y
            "--.."  // z
        };

        Set<String> seen = new HashSet<>();
        for (String w : words) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < w.length(); i++) {
                char c = w.charAt(i);
                int idx = c - 'a';
                sb.append(morse[idx]);
            }
            seen.add(sb.toString());

        }
        return seen.size();
    }
}