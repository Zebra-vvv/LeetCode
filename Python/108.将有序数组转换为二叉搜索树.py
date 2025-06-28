from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 一句话总结：递归地选择有序数组的中间元素作为根节点，左右子数组分别构建左右子树，从而构造一棵高度平衡的二叉搜索树。
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        nums_left = nums[:mid]
        nums_right = nums[mid+1:]

        root.left = self.sortedArrayToBST(nums_left)
        root.right = self.sortedArrayToBST(nums_right)

        return root
