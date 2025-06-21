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
# 一句话总结：使用指针不断向左深入并借助栈记录路径，当左子树到底时回退处理“中”节点，再转向右子树，完成**左-中-右**的中序遍历。

# 和前序遍历的迭代法有区别：前序可以完全依赖一个栈来控制访问顺序；中序需要靠指针走路，栈只是回头用
# 前序靠“栈”控制顺序，中序必须靠“指针 + 栈”组合控制。
class Solution2:
    def inorderTraversal(self, root:TreeNode):
        stack = [] # 因为是”左中右“的遍历顺序，不能把根节点先加入
        result = [] 
        cur = root

        # 如果还没走到底，就往左继续走；走到底了就从栈中弹出处理；直到左也走完，栈也空了，才退出。
        while cur or stack:
            # 一路向左走，把所有左边节点压入栈
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                # 左子树到底后（cur为空），弹出cur，指针回到“中”，开始“中”处理
                # 每个节点的 val 都是 在它自己作为“中”节点 时、从栈中弹出的时候，才被访问和记录的。
                # 所有的节点，都是在执行 result.append(cur.val) 这一行时被收集进结果列表的。
                cur = stack.pop()
                result.append(cur.val)

                # “左”和“中”都处理完了，处理右子树
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

    solution = Solution2()
    result = solution.inorderTraversal(node1)
    print(result)  
    