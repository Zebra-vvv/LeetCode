from typing import List

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# 递归法
class Solution1:
    def preorderTraversal(self, root:TreeNode) -> List[int]:
        self.res = []
        self.dfs(root)
        return self.res
    
    def dfs(self, node):
        
        # 左右孩子都为空
        if not node:
            return
        
        self.res.append(node.val)
        self.dfs(node.left)
        self.dfs(node.right)

# 迭代法
class Solution2:
    def preorderTraversal(self, root:TreeNode) -> List[int]:
        # 根节点为空返回空列表
        if not root:
            return []
        
        stack =  [root]  # 这是一个栈，用于存储待访问的节点，在 Python 中，栈通常使用列表来实现，因为列表具有压栈（append）和出栈（pop）操作，非常适合栈的特性。
        result = []      # 这是一个列表，用于保存遍历的结果
        while stack:
            node = stack.pop()
            result.append(node.val) # 所有结点的值在这里遍历收集到result中去

            # 因为栈LIFO的特性，需要先加入右孩子，再加入左孩子
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return result

if __name__ == "__main__":
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node2 = TreeNode(2, node4, node5)
    node3 = TreeNode(3, node6, node7)
    node1 = TreeNode(1, node2, node3)

    solution = Solution2()
    result = solution.preorderTraversal(node1)
    print(result)