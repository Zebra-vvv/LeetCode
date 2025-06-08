class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.min_diff = float('inf') # 正无穷
        self.pre = None

    def dfs(self, node:TreeNode):

        if not node:
            return
        
        self.dfs(node.left)  # 左

        if self.pre:  # 中
            self.min_diff = min(self.min_diff, node.val - self.pre.val)
        self.pre = node  # 记录前一个

        self.dfs(node.right)  # 右

    def getMinimumDifference(self, root):
        self.dfs(root)
        return self.min_diff
    
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
    result = solution.getMinimumDifference(root1)
    print(result)