class Leaderboard {


    private Map<Integer, Integer> scoreMap;

    public Leaderboard() {
        scoreMap = new HashMap<>();

    }
    
    public void addScore(int playerId, int score) {
        scoreMap.put(playerId, scoreMap.getOrDefault(playerId, 0) + score);
        
    }
    
    public int top(int K) {

        List<Integer> scores = new ArrayList<>(scoreMap.values());
        scores.sort((a, b) -> b - a);
        int sum = 0;
        for (int i = 0; i < K; i++) {
            sum += scores.get(i);
        }
        return sum;
        
    }
    
    public void reset(int playerId) {
        scoreMap.remove(playerId);
    }
}

/**
 * Your Leaderboard object will be instantiated and called as such:
 * Leaderboard obj = new Leaderboard();
 * obj.addScore(playerId,score);
 * int param_2 = obj.top(K);
 * obj.reset(playerId);
 */