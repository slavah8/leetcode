class Solution {
    public int numUniqueEmails(String[] emails) {
        
        Set<String> seen = new HashSet<>();

        for (String email: emails) {
            String[] parts = email.split("@");
            String local = parts[0];
            String domain = parts[1];

            int plusIndex = local.indexOf("+");
            if (plusIndex != -1) {
                local = local.substring(0, plusIndex);
            }

            // remove all . in local
            StringBuilder cleanedLocal = new StringBuilder();
            for (int i = 0; i < local.length(); i++) {
                char c = local.charAt(i);
                if (c != '.') {
                    cleanedLocal.append(c);
                }
            }

            String normalized = cleanedLocal.toString() + '@' + domain;

            seen.add(normalized);
        }
        return seen.size();
    }
}