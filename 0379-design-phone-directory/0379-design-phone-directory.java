class PhoneDirectory {

    private Queue<Integer> freeNumbers;
    private boolean[] used;
    private int maxNumbers;

    public PhoneDirectory(int maxNumbers) {
        this.maxNumbers = maxNumbers;
        this.used = new boolean[maxNumbers];
        this.freeNumbers = new LinkedList<>();

        for (int i = 0; i < maxNumbers; i++) {
            freeNumbers.offer(i);
        }
        
    }
    
    public int get() {
        if (freeNumbers.isEmpty()) {
            return -1;
        }

        int num = freeNumbers.poll();
        used[num] = true;
        return num;
        
    }
    
    public boolean check(int number) {
        if (!used[number]) {
            return true;
        }
        return false;
        
    }
    
    public void release(int number) {
        
        if (number < 0 || number >= maxNumbers) {
            return;
        }
        if (used[number]) {
            used[number] = false;
            freeNumbers.offer(number);
        }
        
    }
}

/**
 * Your PhoneDirectory object will be instantiated and called as such:
 * PhoneDirectory obj = new PhoneDirectory(maxNumbers);
 * int param_1 = obj.get();
 * boolean param_2 = obj.check(number);
 * obj.release(number);
 */