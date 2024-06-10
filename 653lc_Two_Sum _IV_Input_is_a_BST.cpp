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
    bool findTarget(TreeNode* root, int k) {
        unordered_set<int> st;
        return preOrderSearch(st, root, k);
    }

    bool preOrderSearch(unordered_set<int> &st, TreeNode* node, int k){
        if (node == nullptr) return false;
        if(st.find(k-node->val) != st.end()) return true;
        else st.insert(node->val);
        return preOrderSearch(st, node->left, k)|| preOrderSearch(st, node->right,k);
    }
};