class Solution {
    public String generateTheString(int n) {
        StringBuilder sb = new StringBuilder();
        int biggest_odd;
        if (n % 2 == 1) {
            biggest_odd = n;
        } else {
            biggest_odd = n - 1;
        }
        char c = 'a';
        for (int i = 0; i < biggest_odd; i++) {
            sb.append(c);
        }
        
        if (biggest_odd < n) {
            sb.append('b');
        }

        return sb.toString();
    }
}