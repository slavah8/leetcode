/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isUnivalTree(TreeNode root) {
        return dfs(root, root.val);
    }

    private boolean dfs(TreeNode node, int univalue) {
        if (node == null) {
            return true;
        }
        if (node.val != univalue) {
            return false;
        }
        boolean left = dfs(node.left, univalue);
        boolean right = dfs(node.right, univalue);

        return left && right;
    }
}