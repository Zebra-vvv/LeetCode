from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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