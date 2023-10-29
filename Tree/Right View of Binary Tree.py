Right View of Binary Tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recursion(self, root, level, res):
        if not root:
            return
        if len(res) == level:
            res.append(root.val)
        self.recursion(root.right, level + 1, res)
        self.recursion(root.left, level + 1, res)

    def rightSideView(self, root):
        res = []
        self.recursion(root, 0, res)
        return res
.........................................................CPP.............................................
class Solution {
public:
    void recursion(TreeNode *root, int level, vector<int> &res)
    {
        if(root==NULL) return ;
        if(res.size()==level) res.push_back(root->val);
        recursion(root->right, level+1, res);
        recursion(root->left, level+1, res);
    }
    
    vector<int> rightSideView(TreeNode *root) {
        vector<int> res;
        recursion(root, 0, res);
        return res;
    }
};

left View of Binary Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recursion(self, root, level, res):
        if not root:
            return
        if len(res) == level:
            res.append(root.val)
        self.recursion(root.left, level + 1, res)
        self.recursion(root.right, level + 1, res)

    def leftSideView(self, root):
        res = []
        self.recursion(root, 0, res)
        return res


...................................................CPP................................................
class Solution {
public:
    void recursion(TreeNode *root, int level, vector<int> &res)
    {
        if(root==NULL) return ;
        if(res.size()==level) res.push_back(root->val);
        recursion(root->left, level+1, res);
        recursion(root->right, level+1, res);
    }
    
    vector<int> leftSideView(TreeNode *root) {
        vector<int> res;
        recursion(root, 0, res);
        return res;
    }
};
