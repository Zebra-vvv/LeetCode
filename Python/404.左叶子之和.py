from typing import List

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root:TreeNode) -> int:
        if not root:
            return 0 
        return self.dfs(root)
    
    # 递归的遍历顺序为后序遍历（左右中），是因为要通过递归函数的返回值来累加求取左叶子数值之和。
    def dfs(self, node) -> int:
        
        # 当前节点为空时（代表已经递归到底了），就结束这一层的递归。
        if not node:
            return 0
        
        leftSum = self.dfs(node.left)
        rightSum = self.dfs(node.right)

        # 如果当前节点没有左叶子节点，那么本轮递归中要加的值就是 0；
        # 如果当前节点存在一个左叶子节点，就将其值赋给 mid，加到总和里。
        mid = 0
        
        # 左节点存在 并且 左节点的左右孩子都不存在，说明是叶子结点
        if node.left and not node.left.left and not node.left.right:
            mid = node.left.val
        return leftSum + rightSum + mid
    
if __name__ == "__main__":
    # 构建如下的二叉树：
    #       3
    #      / \
    #     9  20
    #        / \
    #       15  7
    #
    # 左叶子节点是 9 和 15，和为 24

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sol = Solution()
    result = sol.sumOfLeftLeaves(root)
    print("左叶子之和为：", result)  # 输出应为 24

