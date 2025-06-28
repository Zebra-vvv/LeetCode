class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 一句话总结：本题采用后序遍历，自底向上查找，若某节点的左右子树分别包含 p 和 q，该节点即为最近公共祖先，否则将非空子树的结果向上传递。
class Solution:
    # 普通二叉树需要自底向上遍历，用后序遍历正好可以满足要求（需要搜索整棵树）
    # 每层节点返回自己所在子树是否有p或q，把这个信息层层向上汇报，直到找到某个节点的左右子树分别有p和q，说明这个节点就是要找的祖先
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None

        # 找到p或q,返回当前节点
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        if left and not right:
            return left

        if not left and right:
            return right

        return None
