class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self,root:TreeNode):
        self.res = []
        self.dfs(root)
        return self.res
    
    def dfs(self,node:TreeNode):
        if node is None:
            return
        self.dfs(node.left)
        self.res.append(node.val)
        self.dfs(node.right)
    
if __name__ == "__main__":
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node2 = TreeNode(2, node4, node5)
    node3 = TreeNode(3, node6, node7)
    node1 = TreeNode(1, node2, node3)

    solution = Solution()
    result = solution.inorderTraversal(node1)
    print(result)  
    