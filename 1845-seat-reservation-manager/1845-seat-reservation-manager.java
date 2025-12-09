class SeatManager {

    private int nextFree;
    private PriorityQueue<Integer> available;

    public SeatManager(int n) {
        this.nextFree = 1;
        this.available = new PriorityQueue<>();
        
    }
    
    public int reserve() {
        if (!available.isEmpty()) {
            return available.poll();
        }
        return nextFree++;
        
    }
    
    public void unreserve(int seatNumber) {
        available.offer(seatNumber);

        
    }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager obj = new SeatManager(n);
 * int param_1 = obj.reserve();
 * obj.unreserve(seatNumber);
 */