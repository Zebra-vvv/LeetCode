from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 一句话总结：本题利用中序遍历二叉搜索树得到有序序列，统计每个值的连续出现次数，并动态维护最大频率 maxCount 与众数列表 result，找出所有众数。
# 利用二叉搜索树的性质：中序遍历下，如果一棵 BST 中有重复值，那么这些重复值一定会挨在一起出现！
class Solution:
    def findMode(self, root) -> List[int]:
        self.count = 0  # 当前值的连续出现次数
        self.maxCount = 0  # 全局最大出现次数
        self.pre = None  # 记录前一个节点
        self.result = []  # 存放众数结果列表

        if not root:
            return []

        self.dfs(root)
        return self.result

    def dfs(self, node: TreeNode):
        if not node:
            return

        self.dfs(node.left)

        if not self.pre:  # pre为空，说明当前开始遍历第一个节点
            self.count = 1
        elif self.pre.val == node.val:
            self.count += 1
        else:  # 当前节点和前一个节点不相等
            self.count = 1
        self.pre = node  # pre向后移动

        if self.count == self.maxCount:
            self.result.append(node.val)

        elif self.count > self.maxCount:
            self.maxCount = self.count  # 更新 maxCount
            self.result = []  # 必须先清空之前的结果，因为现在出现了更大的 maxCount
            self.result.append(node.val)

        self.dfs(node.right)


if __name__ == "__main__":
    # 手动构建一棵BST（题目要求，所以有重复值）
    #       1
    #        \
    #         2
    #        /
    #       2
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(2)

    solution = Solution()
    result = solution.findMode(root)
    print(result)
