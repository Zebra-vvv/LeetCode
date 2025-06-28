from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 一句话总结：本题利用**前序遍历确定根节点、中序遍历划分左右子树，递归构建整棵二叉树，关键在于正确切割两个数组，保持元素对应关系。
class Solution:
    # 105和106题，力扣上传参是反的，注意一下！
    def buildTree(self, preorder:List[int], inorder:List[int]) -> TreeNode:

        if not preorder:
            return None
        
        root_val = preorder[0]
        root = TreeNode(root_val)

        mid = inorder.index(root_val)

        inorder_left = inorder[:mid]
        inorder_right = inorder[mid+1:]

        preorder_left = preorder[1:len(inorder_left)+1]
        preorder_right = preorder[len(inorder_left)+1:]

        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root