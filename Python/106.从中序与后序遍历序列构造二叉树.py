from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 一句话总结：一句话总结：本题通过**后序遍历确定根节点、中序遍历定位左右子树边界**，递归构建整棵二叉树，关键在于正确切割中序和后序数组以还原树结构。
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # 第一步: 特殊情况讨论，树为空(递归的终止条件)
        if not postorder:
            return None

        # 第二步: 后序遍历的最后一个就是当前子树的根节点，针对当前子树叫root_val没问题，不需要改为node_val
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # 第三步: 找切割点.
        mid = inorder.index(root_val)  # .index 会返回该根节点在中序遍历数组中的下标 mid

        # 第四步: 切割inorder数组. 得到inorder数组的左,右半边.
        # [左子树..., 根, 右子树...]：需要去掉根节点，所以inorder_right从mid+1开始
        # 数组切片用冒号，切片是左闭右开的
        inorder_left = inorder[:mid]
        inorder_right = inorder[mid + 1:]

        # 第五步: 切割postorder数组. 得到postorder数组的左,右半边.
        # [左子树..., 右子树..., 根]：需要去掉根节点，所以postorder_right的切到-1（最后一个元素）
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left):-1]

        # 第六步: 递归
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        # 第七步: 返回答案
        return root

    # 中序遍历模板，用于验证结果的

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        self.dfs(root)
        return self.res

    def dfs(self, node: TreeNode):
        if not node:
            return

        self.dfs(node.left)
        self.res.append(node.val)
        self.dfs(node.right)


if __name__ == "__main__":
    solution = Solution()

    # 示例输入
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]

    # 构建二叉树
    root = solution.buildTree(inorder, postorder)

    result = solution.inorderTraversal(root)
    print(result)
