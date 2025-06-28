from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 一句话总结：本题通过递归方式将两棵树对应节点相加，在 root1 上进行原地修改并合并其左右子树，最终返回合并后的新树。
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:

        # root1 或 root2 其中一个为空，直接取另一个
        if not root1:
            return root2
        if not root2:
            return root1

        # root1 和 root2 均不为空，直接在root1上原地修改
        root1.val += root2.val

        # 递归合并左右子树
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1
