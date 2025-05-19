from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right 

# 层序遍历的模板来解决
class Solution:
    def rightSideView(self, root:TreeNode) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        result = []
        
        while queue:
            size = len(queue) 
            for i in range(size):
                node = queue.popleft()

                if i == size - 1: # 遍历到最后一个节点再收集
                    result.append(node.val) 

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
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
    result = solution.rightSideView(node1)
    print(result)