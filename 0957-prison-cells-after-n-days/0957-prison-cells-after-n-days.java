class Solution {
    public int[] prisonAfterNDays(int[] cells, int n) {
        
        Map<String, Integer> seen = new HashMap<>();
        
        List<int[]> states = new ArrayList<>();

        while (n > 0) {
            String key = Arrays.toString(cells);
            
            if (seen.containsKey(key)) {
                int firstIndex = seen.get(key);
                int cycleLen = states.size() - firstIndex;

                n %= cycleLen;
                break;
            }

            seen.put(key, states.size());
            states.add(cells.clone());
            cells = nextDay(cells);
            n--;
        }

    while (n > 0) {
        cells = nextDay(cells);
        n--;
    }
    return cells;

    }

    private int[] nextDay(int[] cells) {
        int[] next = new int[8];
        next[0] = 0;
        next[7] = 0;
        for (int i = 1; i < 7; i++) {
            next[i] = (cells[i - 1] == cells[i + 1]) ? 1 : 0;
        }
        return next;
    }
}