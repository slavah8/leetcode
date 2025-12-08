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
    public ListNode reverseEvenLengthGroups(ListNode head) {
        ListNode dummy = new ListNode(0, head);
        ListNode prevTail = dummy;
        ListNode curr = head;

        int groupSize = 1;

        while (curr != null) {
            int count = 0;
            ListNode temp = curr;

            while (count < groupSize && temp != null) {
                temp = temp.next;
                count++;
            }

            int groupLen = count;
            ListNode nextHead = temp;

            if (groupLen % 2 == 0) {
                // reverse this group starting at curr
                ListNode node = curr;
                ListNode prev = nextHead;

                for (int i = 0; i < groupLen; i++) {
                    ListNode nextNode = node.next;
                    node.next = prev;
                    prev = node;
                    node = nextNode;
                }

                prevTail.next = prev;
                prevTail = curr;
                curr = nextHead;
            } else {
                for (int i = 0; i < groupLen; i++) {
                    prevTail = curr;
                    curr = curr.next;
                }
            }

            groupSize++;
        }

        return dummy.next;
    }
}