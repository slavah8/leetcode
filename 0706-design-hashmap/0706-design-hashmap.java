class MyHashMap {

    private static class Node {
        int key;
        int value;
        Node next;

        Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    private static final int SIZE = 10000; // number of buckets
    private Node[] buckets;

    public MyHashMap() {
        buckets = new Node[SIZE];
    }

    private int hash(int key) {
        return key % SIZE;
    }

    // Ensure bucket has a dummy head and return it
    private Node getDummyHead(int index) {
        if (buckets[index] == null) {
            buckets[index] = new Node(-1, -1); // dummy node
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

    public void put(int key, int value) {
        int index = hash(key);
        Node prev = findPrev(key, index);
        if (prev.next == null) {
            // key not present, insert new node
            prev.next = new Node(key, value);
        } else {
            // key exists, update value
            prev.next.value = value;
        }
    }

    public int get(int key) {
        int index = hash(key);
        Node prev = findPrev(key, index);
        if (prev.next == null) {
            return -1; // not found
        }
        return prev.next.value;
    }

    public void remove(int key) {
        int index = hash(key);
        Node prev = findPrev(key, index);
        if (prev.next != null) {
            // unlink the node
            prev.next = prev.next.next;
        }
    }
}


/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */