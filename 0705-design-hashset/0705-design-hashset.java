class MyHashSet {

    private static class Node {
        int key;
        Node next;

        Node(int key) {
            this.key = key;
        }
    }

    private static final int SIZE = 10000;
    private Node[] buckets;

    public MyHashSet() {
        buckets = new Node[SIZE];
    }

    private int hash(int key) {
        return key % SIZE;
    }

    // Ensure bucket at index has a dummy head and return it
    private Node getDummyHead(int index) {
        if (buckets[index] == null) {
            buckets[index] = new Node(-1); // dummy node
        }
        return buckets[index];
    }

    // Find the previous node of the node with "key" in bucket[index]
    // If not found, returns the last node in the list
    private Node findPrev(int key, int index) {
        Node dummy = getDummyHead(index);
        Node curr = dummy;
        while (curr.next != null && curr.next.key != key) {
            curr = curr.next;
        }
        return curr;
    }

    public void add(int key) {
        int index = hash(key);
        Node prev = findPrev(key, index);
        if (prev.next == null) {
            // key not present, insert new node
            prev.next = new Node(key);
        }
        // if prev.next != null, key already exists -> do nothing
    }

    public void remove(int key) {
        int index = hash(key);
        Node prev = findPrev(key, index);
        if (prev.next != null) {
            // key exists, unlink it
            prev.next = prev.next.next;
        }
    }

    public boolean contains(int key) {
        int index = hash(key);
        Node prev = findPrev(key, index);
        return prev.next != null;  // if not null, key exists
    }
}


/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */