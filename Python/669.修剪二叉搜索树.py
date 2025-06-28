from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 一句话总结：递归剪枝二叉搜索树，遇到不在区间内的节点就直接“裁掉”，其子树向上传递合法部分，最终层层拼接回合法树结构
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:

        # 真正删除的精髓，就是这个return None
        if not root:
            return None  # 真正把当前节点“删掉”

        # 当前节点小于下限，但是右子树中可能还有合法的节点，需要递归右子树
        if root.val < low:
            return self.trimBST(root.right, low, high)

        # 当前节点大于上限，但是左子树中可能还有合法的节点，需要递归左子树
        if root.val > high:
            return self.trimBST(root.left, low, high)

        # 上一层接住下层的合法子树
        root.left = self.trimBST(root.left, low, high)  # root.left 接入符合条件的左孩子

        # root.right 接入符合条件的右孩子
        root.right = self.trimBST(root.right, low, high)

        return root
