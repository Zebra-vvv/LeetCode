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
        
        # 当前节点为空时（代表已经递归到底了），就结束这一层的递归。
        if not node:
            return
        
        self.res.append(node.val) # self 是当前对象（类实例）本身，它的属性可以在这个类的所有方法中共享访问
        self.dfs(node.left)
        self.dfs(node.right)

# 迭代法
# 一句话总结：使用栈来模拟递归的过程，先将根节点入栈，每次弹出栈顶节点并记录其值，然后先将右子节点入栈，再将左子节点入栈，确保出栈顺序为“根-左-右”，从而实现前序遍历。
class Solution2:
    def preorderTraversal(self, root:TreeNode) -> List[int]:
        
        # 根节点为空直接返回空列表
        if not root:
            return []
        
        stack =  [root]  # 这是一个栈，用于存储待访问的节点
        result = []      # 这是一个列表，用于保存遍历的结果
        while stack:
            node = stack.pop()
            result.append(node.val) # 所有结点的值在这里遍历收集到result中去

            # 因为栈LIFO的特性，需要先加入右孩子，再加入左孩子，这样出栈的时候才是“中左右“的顺序
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