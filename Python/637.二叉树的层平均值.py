from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right 

# 一句话总结：层序遍历模板，每层计算一下平均值就行了
class Solution:
    def averageOfLevels(self, root:TreeNode) -> List[int]: 
        if not root:
            return []

        queue = deque([root]) 
        result = [] 
        
        while queue:
            level_sum = 0
            size = len(queue) 
            for _ in range(size):
                node = queue.popleft()
                level_sum += node.val # 把每层所有节点的值加和
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            avg = level_sum / size # 算出这一层的平均值
            result.append(avg)

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
    result = solution.averageOfLevels(node1)
    print(result)
