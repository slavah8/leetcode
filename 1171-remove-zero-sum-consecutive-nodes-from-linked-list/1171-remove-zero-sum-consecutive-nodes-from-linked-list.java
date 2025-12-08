/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeZeroSumSublists(ListNode head) {

        ListNode dummy = new ListNode(0);
        dummy.next = head;

        Map<Integer, ListNode> prefixtoNode = new HashMap<>();
        int prefix = 0;
        ListNode node = dummy;

        while (node != null) {
            prefix += node.val;
            prefixtoNode.put(prefix, node);
            node = node.next;
        }

        prefix = 0;
        node = dummy;

        while (node != null) {
            prefix += node.val;
            ListNode last = prefixtoNode.get(prefix);

            node.next = last.next;
            node = node.next;

        }
        return dummy.next;
        

    }
}