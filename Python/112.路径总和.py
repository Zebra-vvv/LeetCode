from typing import List

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, node, path, targetSum) -> bool:

        # 采用前序遍历，“一边走一边记录路径”，每次进入一个节点就能立即记录它在路径上的位置。
        path.append(node.val)  # 中

        if not node.left and not node.right:  # 到达叶子节点，说明这是一条完整路径，进行判断
            if sum(path) == targetSum:
                return True
        
        if node.left:  # 左
            if self.dfs(node.left, path, targetSum):
                return True # 找到了就提前返回，不继续递归
            path.pop()  
        if node.right:  # 右 
            if self.dfs(node.right, path, targetSum):
                return True # 找到了就提前返回，不继续递归
            path.pop()  

        # 左右子树都没找到符合条件的路径
        return False

    def hasPathSum(self, root:TreeNode, targetSum:int) -> bool:
        path = [] 
        if not root:
            return False
        return self.dfs(root, path, targetSum)
    
if __name__ == "__main__":
    node5 = TreeNode(5)
    node2 = TreeNode(2, None, node5)
    node3 = TreeNode(3)
    root = TreeNode(1, node2, node3)

    solution = Solution()
    paths = solution.hasPathSum(root,)
    
