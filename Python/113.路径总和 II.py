from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 一句话总结：本题与上一题的区别在于需要遍历所有路径并记录，不提前返回，而是将满足条件的路径副本加入结果中，并通过 path.pop() 回溯继续搜索其它可能路径。
# 因为要遍历所有二叉树组合，不需要返回值，注意list(path)这个地方
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        self.result = []
        path = []
        self.dfs(root, path, targetSum)
        return self.result

    def dfs(self, node, path, targetSum):
        if not node:
            return

        # 中
        path.append(node.val)
        if not node.left and not node.right:
            if sum(path) == targetSum:

                # list(path) 创建了一份当前路径的副本，避免回溯后对结果的污染
                self.result.append(list(path))

        # 左
        self.dfs(node.left, path, targetSum)

        # 右
        self.dfs(node.right, path, targetSum)

        # 回溯
        path.pop()
