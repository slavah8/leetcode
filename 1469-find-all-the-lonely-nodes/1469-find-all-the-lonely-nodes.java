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
    private List<Integer> lonely = new ArrayList<>();
    public List<Integer> getLonelyNodes(TreeNode root) {
        dfs(root);
        return lonely;
    }

    private void dfs(TreeNode node) {
        
        if (node == null) {
            return;
        }
        if (node.left != null && node.right == null) {
            lonely.add(node.left.val);
        } 
        if (node.left == null && node.right != null) {
            lonely.add(node.right.val);
        }

        dfs(node.left);
        dfs(node.right);
    }
}