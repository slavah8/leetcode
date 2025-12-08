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
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        List<Integer> critical = new ArrayList<>();
        int[] res = new int[] { -1, -1 };

        if (head == null || head.next == null || head.next.next == null) {
            return res;
        }

        int idx = 1;
        ListNode prev = head;
        ListNode curr = head.next;

        while (curr != null && curr.next != null) {
            int prev_val = prev.val;
            int curr_val = curr.val;
            int next_val = curr.next.val;

            boolean is_max = curr_val > prev_val && curr_val > next_val;
            boolean is_min = curr_val < prev_val && curr_val < next_val;

            if (is_max || is_min) {
                critical.add(idx);
            }

            prev = curr;
            curr = curr.next;
            idx++;
        }

        if (critical.size() < 2) {
            return res;
        }

        int max_dist = critical.get(critical.size() - 1) - critical.get(0);

        int min_dist = Integer.MAX_VALUE;
        for (int i = 1; i < critical.size(); i++) {
            int diff = critical.get(i) - critical.get(i - 1);

            if (diff < min_dist) {
                min_dist = diff;
            }
        }

        res[0] = min_dist;
        res[1] = max_dist;
        return res;
    }
}