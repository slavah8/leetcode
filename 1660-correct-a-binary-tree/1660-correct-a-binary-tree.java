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
import java.util.Queue;
import java.util.LinkedList;
import java.util.HashSet;
import java.util.Set;

class Solution {

    // Helper class to keep track of node + its parent + whether it's a left child
    private static class NodeInfo {
        TreeNode node;
        TreeNode parent;
        boolean isLeft;   // true if this node is parent's left child

        NodeInfo(TreeNode node, TreeNode parent, boolean isLeft) {
            this.node = node;
            this.parent = parent;
            this.isLeft = isLeft;
        }
    }

    public TreeNode correctBinaryTree(TreeNode root) {
        if (root == null) return null;

        Queue<NodeInfo> q = new LinkedList<>();
        Set<TreeNode> visited = new HashSet<>();

        // Start BFS from root; root has no parent
        q.offer(new NodeInfo(root, null, false));

        while (!q.isEmpty()) {
            NodeInfo info = q.poll();
            TreeNode node = info.node;

            // If node's right child points to a node we've already visited,
            // this node is the invalid one.
            if (node.right != null && visited.contains(node.right)) {
                // Remove this node from its parent
                if (info.parent != null) {
                    if (info.isLeft) {
                        info.parent.left = null;
                    } else {
                        info.parent.right = null;
                    }
                } else {
                    // Edge case: invalid node is root (usually not in test cases)
                    // If needed, you could decide what to return here.
                    root = null;
                }
                break;
            }

            // Mark this node as visited after we checked its right pointer
            visited.add(node);

            // IMPORTANT: push right child first so we traverse levels right-to-left
            if (node.right != null) {
                q.offer(new NodeInfo(node.right, node, false));
            }
            if (node.left != null) {
                q.offer(new NodeInfo(node.left, node, true));
            }
        }

        return root;
    }
}
