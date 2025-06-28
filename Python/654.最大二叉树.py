from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 一句话总结：本题通过递归寻找当前数组中的最大值作为根节点，将数组左右两部分分别构建左、右子树，最终构造出最大二叉树。
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:

        if not nums:
            return None

        max_val = max(nums)
        root = TreeNode(max_val)

        mid = nums.index(max_val)

        nums_left = nums[:mid]
        nums_right = nums[mid+1:]

        root.left = self.constructMaximumBinaryTree(nums_left)
        root.right = self.constructMaximumBinaryTree(nums_right)

        return root
