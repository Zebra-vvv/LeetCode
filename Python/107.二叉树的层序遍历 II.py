from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right 

class Solution:
    def levelOrderBottom(self,root:TreeNode) -> List[List[int]]: # 要分层返回，所以是2层List
        if not root:
            return []

        queue = deque([root]) # TreeNode 是个普通类，不是可迭代对象，要用列表包一层。
        result = [] # 存放最终结果
        
        # 总之就是pop一个节点的同时，加入它的左右孩子
        while queue:
            level = [] # 存放每层的结果
            size = len(queue) # 每层的节点数

            # for循环执行1次，收集一个节点；整个for循环结束之后，收集一层节点
            for i in range(size):
                node = queue.popleft()
                level.append(node.val) # 收集本层节点
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level) # 把当前层的节点加入最终结果
        
        return result[::-1] # 把正常层序遍历逆序输出即可
    
if __name__ == "__main__":
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node2 = TreeNode(2, node4, node5)
    node3 = TreeNode(3, node6, node7)
    node1 = TreeNode(1, node2, node3)
    solution = Solution()
    result = solution.levelOrderBottom(node1)
    print(result)
