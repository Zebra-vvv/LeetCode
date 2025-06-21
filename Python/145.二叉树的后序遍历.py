class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 递归法
class Solution1:
    def postorderTraversal(self, root:TreeNode):
        self.res = []
        self.dfs(root)
        return self.res
    
    def dfs(self,node:TreeNode):
        if not node:
            return
        self.dfs(node.left)
        self.dfs(node.right)
        self.res.append(node.val)

# 一句话总结：在前序迭代法的基础上，更换左右收集顺序并反转result列表，即可实现后序迭代法：中左右 -> 中右左 -> 左右中
# 迭代法
class Solution2:
    
    def postorderTraversal(self, root:TreeNode):
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]


if __name__ == "__main__":
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node2 = TreeNode(2, node4, node5)
    node3 = TreeNode(3, node6, node7)
    node1 = TreeNode(1, node2, node3)

    solution = Solution2()
    result = solution.postorderTraversal(node1)
    print(result)  
    