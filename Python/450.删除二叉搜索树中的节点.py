from typing import List

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root:TreeNode, key:int) -> TreeNode:
        if not root:
            return None
        
        # 根据二叉搜索树的性质，在左右子树中递归查找
        if key < root.val:
            # 每一层都要将“修改过的子树”重新赋值给当前节点的 .left 或 .right，否则就相当于“没删除成功”。
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        # 找到了要删除的节点
        else:

            # 如果是叶子节点，直接 return None 给上一层，就等价于把这个节点删掉了
            if not root.right and not root.left:
                return None
            
            # 如果这个节点的左右子树有一个为空，直接用非空的子树替代被删的节点
            if not root.right and root.left:
                return root.left
            elif root.right and not root.left:
                return root.right
            
            # 如果左右子树都不为空
            else:
                # 用cur寻找被删节点右子树中最左下角的节点（中序遍历后继节点）
                cur = root.right
                while cur.left:
                    cur = cur.left

                # 然后将多出来的左子树挂在右子树中最左下角的节点下面
                cur.left = root.left

                # 用右子树顶替当前被删节点的位置
                return root.right 

        return root