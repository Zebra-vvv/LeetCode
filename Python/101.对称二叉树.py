class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root:TreeNode) -> bool:
        if not root:
            return True
        left = root.left
        right = root.right
        return self.compare(left, right)

    # compare函数作用：比较两个子树是否互为镜像
    def compare(self, left:TreeNode, right:TreeNode):
        # 处理空节点的边界情况
        if left == None and right != None:
            return False
        elif left != None and right == None:
            return False
        
        # 终止条件：遍历到树的底部了，左右子树仍然相等
        elif left == None and right == None:
            return True
        
        # 排除值不相等的情况
        elif left.val != right.val:
                return False
        
        # 递归判断下一层
        outside = self.compare(left.left, right.right)
        inside = self.compare(left.right, right.left)
        isSame = outside and inside
        return isSame
    
if __name__ == "__main__":
    # 测试用例1：对称树
    '''
        1
       / \
      2   2
     / \ / \
    3  4 4  3
    '''
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(3)

    solution = Solution()
    result = solution.isSymmetric(root1)
    print(result)
