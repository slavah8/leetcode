/*
// Definition for a Node.
class Node {
    public int val;
    public Node next;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _next) {
        val = _val;
        next = _next;
    }
};
*/

class Solution {
    public Node insert(Node head, int insertVal) {
        // Case 0: empty list → create a single circular node
        if (head == null) {
            Node node = new Node(insertVal);
            node.next = node;
            return node;
        }

        Node curr = head;
        boolean inserted = false;

        do {
            Node next = curr.next;

            // Case 1: normal increasing region: curr.val <= next.val
            // insertVal fits between them (sorted)
            if (curr.val <= insertVal && insertVal <= next.val) {
                inserted = true;
            }
            // Case 2: pivot region: curr.val > next.val (max -> min)
            // insertVal is either >= max or <= min
            else if (curr.val > next.val) {
                if (insertVal >= curr.val || insertVal <= next.val) {
                    inserted = true;
                }
            }

            if (inserted) {
                Node node = new Node(insertVal);
                curr.next = node;
                node.next = next;
                return head;
            }

            curr = curr.next;
        } while (curr != head);  // stop after one full loop

        // Case 3: we didn't find any special spot (e.g., all values equal)
        // insert anywhere, say after head
        Node node = new Node(insertVal);
        node.next = head.next;
        head.next = node;
        return head;
    }
}
