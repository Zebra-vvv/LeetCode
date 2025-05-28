class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root:TreeNode) -> TreeNode:
        self.dfs(root)
        return root
    
    def dfs(self, node:TreeNode):
        
        if not node:
            return
        
        tmp = node.left
        node.left = node.right
        node.right = tmp
        self.dfs(node.left)
        self.dfs(node.right)