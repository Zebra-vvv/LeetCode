from typing import List

class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right 

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # 为什么要有返回值: 
        #   因为搜索到目标节点就要立即return，
        #   这样才是找到节点就返回（搜索某一条边），如果不加return，就是遍历整棵树了。

        if not root or root.val == val: 
            return root

        if root.val > val:
            return self.searchBST(root.left, val)

        if root.val < val: 
            return self.searchBST(root.right, val)

        # 最后不用return None，前面的判断逻辑已经都包含了