from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 一句话总结：层序遍历模板，每层累加depth即可
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        que = deque([root])
        depth = 0
        while que:
            size = len(que)
            depth += 1
            for _ in range(size):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return depth

if __name__ == "__main__":
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node2 = TreeNode(2, node4, node5)
    node3 = TreeNode(3, node6, node7)
    node1 = TreeNode(1, node2, node3)
    solution = Solution()
    result = solution.maxDepth(node1)
    print(result)