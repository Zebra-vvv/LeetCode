from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
        
