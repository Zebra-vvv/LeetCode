class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 递归法   
class Solution1:
    def inorderTraversal(self, root:TreeNode):
        self.res = []
        self.dfs(root)
        return self.res
    
    def dfs(self,node:TreeNode):
        if node is None:
            return
        self.dfs(node.left)
        self.res.append(node.val)
        self.dfs(node.right)

# 迭代法
class Solution2:
    def inorderTraversal(self, root:TreeNode):
        stack = [] # 因为是”左中右“的遍历顺序，不能把根节点先加入
        result = [] 
        cur = root
        while cur or stack:
            # 先找到最左下角的结点
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                # cur.left为空，处理”中“的逻辑，收集元素
                cur = stack.pop()
                result.append(cur.val)
                # ”左“和”中“处理完了，应该处理”右“
                cur = cur.right
        return result
    
if __name__ == "__main__":
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node2 = TreeNode(2, node4, node5)
    node3 = TreeNode(3, node6, node7)
    node1 = TreeNode(1, node2, node3)

    solution = Solution3()
    result = solution.inorderTraversal(node1)
    print(result)  
    