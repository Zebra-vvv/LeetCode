class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# 一句话总结：用后序遍历，每个节点向上汇报自己是否平衡
class Solution:
    def isBalanced(self, root:TreeNode) -> bool:
        if self.dfs(root) != -1:
            return True
        else:
            return False
    
    def dfs(self, node) -> int:
        if not node:
            return 0
      
        # 后序遍历
        leftHeight= self.dfs(node.left) # 左
        rightHeight= self.dfs(node.right) # 右

        # 中
        # 如果左子树或者右子树已经不平衡了，无需继续遍历，直接返回-1
        # 如果当前节点的左右子树高度差大于1，直接返回-1
        if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
            return -1 # 返回-1：当前节点的左右子树不平衡
        
        return max(leftHeight, rightHeight) + 1 # 返回当前节点高度：左右子树中高的那个再+1
    
if __name__ == "__main__":
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
    result = solution.isBalanced(root)
    print(result)