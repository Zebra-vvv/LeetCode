from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 一句话总结：通过反中序遍历（二叉搜索树的右-根-左顺序）累加节点值，将二叉搜索树转换为累加树。
# ✅ 为什么用反中序遍历（右-根-左）？
# 中序遍历（左 → 根 → 右） 会以 升序 访问 BST 中的节点。
# 那么 反中序遍历（右 → 根 → 左） 就会以 降序 顺序访问 BST 中的节点。
# 这正好符合「累加树」的需求：每个节点值需要加上它 右边所有节点的值之和（比它大的所有值）
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        self.pre = 0  # 记录前一个节点的数值
        self.dfs(root)
        return root

    def dfs(self, node: TreeNode):
        if not node:
            return

        # 右
        self.dfs(node.right)

        # 中
        node.val += self.pre
        self.pre = node.val

        # 左
        self.dfs(node.left)
