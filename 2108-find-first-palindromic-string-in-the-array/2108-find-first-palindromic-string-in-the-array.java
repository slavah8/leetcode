class Solution {
    public String firstPalindrome(String[] words) {
        for (String w : words) {
            if (is_palindrome(w)) {
                return w;
            }
        }
        return "";
    }

    public boolean is_palindrome(String s) {
        int l = 0;
        int r = s.length() - 1;

        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) {
                return false;
            } 
            l++;
            r--;
        }
        return true;
    }
}

