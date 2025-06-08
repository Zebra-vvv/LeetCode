class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# 关键思路：中序遍历二叉搜索树，一定是一个升序数组！
class Solution:
    def __init__(self):
        self.pre = None  # 设置为实例变量，递归中共享

    def isValidBST(self, root:TreeNode) -> bool:
        
        # 一个空节点，也算是二叉搜索树
        # 也会层层向上返回 True，直到遇到不合法的情况才会中途返回 False
        if not root:
            return True
        
        left = self.isValidBST(root.left) # 左

        # 中
        if self.pre and self.pre.val >= root.val:
            return False
        self.pre = root # pre 按照中序遍历顺序往后移动一个节点
        
        right = self.isValidBST(root.right) # 右

        return left and right # 左右子树都符合，整棵树才符合


if __name__ == "__main__":
    # 测试用例
    '''
        5
       / \
      2   10
     / \ / \
    1  3 8  12
    '''
    root1 = TreeNode(5)
    root1.left = TreeNode(2)
    root1.right = TreeNode(10)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(3)
    root1.right.left = TreeNode(8)
    root1.right.right = TreeNode(12)

    solution = Solution()
    result = solution.isValidBST(root1)
    print(result)
      