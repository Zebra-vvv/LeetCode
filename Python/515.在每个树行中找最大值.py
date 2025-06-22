from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

# 一句话总结：层序遍历模板，只收集每行的最大值
class Solution:
    def largestValues(self, root:TreeNode) -> List[int]:
        if not root:
            return []
        que = deque([root])
        result = []
        while que:
            max_val = float('-inf') # 定义负无穷，方便后续比较出最大值
            size = len(que)
            for _ in range(size):
                node = que.popleft() # 一定要记住，队列要popleft，而不是pop

                max_val = max(max_val, node.val) # 只维护每行最大值

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            result.append(max_val)
        return result

if __name__ == "__main__":
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node2 = TreeNode(2, node4, node5)
    node3 = TreeNode(3, node6, node7)
    node1 = TreeNode(1, node2, node3)
    solution = Solution()
    result = solution.largestValues(node1)
    print(result)


                