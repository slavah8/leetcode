class NumberContainers {

    private Map<Integer, Integer> idxToNum;
    private Map<Integer, PriorityQueue<Integer>> numToHeap;
    public NumberContainers() {
        idxToNum = new HashMap<>();
        numToHeap = new HashMap<>();
        
    }
    
    public void change(int index, int number) {

        idxToNum.put(index, number);

        numToHeap.putIfAbsent(number, new PriorityQueue<>());
        numToHeap.get(number).offer(index);
        
    }
    
    public int find(int number) {
        PriorityQueue<Integer> heap = numToHeap.get(number);

        if (heap == null) {
            return -1;
        }

        while (!heap.isEmpty() && !idxToNum.get(heap.peek()).equals(number)) {
            heap.poll();
        }

        
        if (heap.isEmpty()) {
            return -1;
        }
        return heap.peek();
        
    }
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers obj = new NumberContainers();
 * obj.change(index,number);
 * int param_2 = obj.find(number);
 */