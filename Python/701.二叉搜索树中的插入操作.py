from typing import List

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# ✅ 插入操作只会“加节点”，不会“改节点”，并且
# ❗ 替换是删除操作中才需要的技巧，用于保持 BST 结构。
class Solution:
    def insertIntoBST(self, root:TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        self.dfs(root, val)
        return root

    def dfs(self, root, val):
        if not root:
            return
        
        if root.val < val:
            # 右子树不为空，继续递归右子树
            if root.right:
                self.dfs(root.right, val)
            
            # 右子树为空，直接插入
            else:
                root.right = TreeNode(val)
                return 

        elif root.val > val:
            if root.left:
                self.dfs(root.left, val)
            else:
                root.left = TreeNode(val)
                return