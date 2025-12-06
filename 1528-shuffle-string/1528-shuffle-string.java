class Solution {
    public String restoreString(String s, int[] indices) {
        int n = s.length();
        char[] res = new char[n];
        for (int i = 0; i < n; i++) {
            int idx = indices[i];
            res[idx] = s.charAt(i);
        }
        return new String(res);
    }
    
}