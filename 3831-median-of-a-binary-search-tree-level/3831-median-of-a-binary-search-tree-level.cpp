/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int levelMedian(TreeNode* root, int level) {
        if (!root) return -1;

        queue<TreeNode*> q;
        q.push(root);
        int curr_level = 0;
        vector<int> arr;
        bool ok = false;

        while (!q.empty()) {
            int size = q.size();

            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();

                if (curr_level == level) {
                    arr.push_back(node->val);
                }
                if (node->left) {
                    q.push(node->left);
                }
                if (node->right) {
                    q.push(node->right);
                }
            }

        if (level == curr_level) {
            if (arr.empty()) return -1;

            sort(arr.begin(), arr.end());
            int idx = arr.size() / 2;
            return arr[idx];
        }
        curr_level++;
        }
        return -1;
    }
};