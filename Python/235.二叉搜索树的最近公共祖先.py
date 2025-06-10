class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right 

# 二叉搜索树为什么是从上到下遍历？（可以和当前节点比较大小来剪枝，不需要搜索整棵树）
# 第一步就是判断当前根节点 root 是否是公共祖先（即判断 p 和 q 是否在它的两侧）；
# 如果不是，就根据 BST 的性质向左子树或右子树递归；
# 每一步都是先判断当前节点，再决定是否向下走，直到找到最小的那个“交汇点”，这就是最近公共祖先。
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        if not root:
            return None
        
        # 当前节点大于p和q，说明p和q都在当前节点的左子树中，递归左子树的结果一定不为空，所以不需要判空
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
            
        # 当前节点小于p和q，说明p和q都在当前节点的右子树中
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # p和q分别位于当前节点的左右子树中，说明当前就是最近的祖先节点
        return root