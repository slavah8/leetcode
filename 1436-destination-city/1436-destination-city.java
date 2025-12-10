class Solution {
    public String destCity(List<List<String>> paths) {
        
        Set<String> starts = new HashSet<>();

        for (List<String> path : paths) {
            String from = path.get(0);
            starts.add(from);
        }

        for (List<String> path : paths) {
            String to = path.get(1);
            if (!starts.contains(to)) {
                return to;
            }
        }
        return "";
    }
}