class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right 

# 一句话总结：用后序遍历，因为每一个节点都向上汇报自己的结果，直到汇报到根节点，就知道总数了
class Solution:
    def countNodes(self, root:TreeNode) -> int:
        if not root:
            return 0
        return self.dfs(root)
   
    # 这种问题使用后序遍历更加通用
    # 比如：求树的最大深度、求是否平衡、判断对称结构
    def dfs(self, node) -> int:
        if not node:
            return 0
        
        # 后序遍历
        leftNum = self.dfs(node.left) # 左
        rightNum = self.dfs(node.right) # 右
        treeNum = leftNum + rightNum + 1 # 中，在“中“的处理逻辑中加和
        return treeNum
    
if __name__ == "__main__":
    # 构造一个完全二叉树：
    #        1
    #      /   \
    #     2     3
    #    / \   /
    #   4   5 6

    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node2 = TreeNode(2, node4, node5)
    node3 = TreeNode(3, node6)
    root = TreeNode(1,node2,node3)

    solution = Solution()
    count = solution.countNodes(root)
    print("节点数:", count)  # 预期输出为 6
