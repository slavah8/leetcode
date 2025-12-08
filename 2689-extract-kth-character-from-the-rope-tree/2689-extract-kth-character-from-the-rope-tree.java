/**
 * Definition for a rope tree node.
 * class RopeTreeNode {
 *     int len;
 *     String val;
 *     RopeTreeNode left;
 *     RopeTreeNode right;
 *     RopeTreeNode() {}
 *     RopeTreeNode(String val) {
 *         this.len = 0;
 *         this.val = val;
 *     }
 *     RopeTreeNode(int len) {
 *         this.len = len;
 *         this.val = "";
 *     }
 *     RopeTreeNode(int len, RopeTreeNode left, RopeTreeNode right) {
 *         this.len = len;
 *         this.val = "";
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public char getKthCharacter(RopeTreeNode root, int k) {
        return dfs(root, k);
    }

    private char dfs(RopeTreeNode node, int k) {
        if (node.left == null && node.right == null) {
            return node.val.charAt(k - 1);
        }

        int leftLen = getLen(node.left);

        if (k <= leftLen) {
            return dfs(node.left, k);
        } else {
            return dfs(node.right, k - leftLen);
        }
    }

    private int getLen(RopeTreeNode node) {
        if (node == null) {
            return 0;
        }

        if (node.left == null && node.right == null) {
            return node.val.length();
        }

        return node.len;
    }
}