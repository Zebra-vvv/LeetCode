from typing import List

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# 一句话总结：前序遍历最方便，因为它的访问顺序天然就是一条从根到底的路径构建顺序，非常适合记录和处理“根到叶”的路径类问题，注意递归回溯不能漏写了
class Solution:
    def binaryTreePaths(self, root:TreeNode) -> List[str]:
        result = []
        path = []
        if not root:
            return result
        self.dfs(root, path, result)
        return result

    def dfs(self, node, path, result):

        # 采用前序遍历，“一边走一边记录路径”，每次进入一个节点就能立即记录它在路径上的位置。
        path.append(node.val)  # 中

        if not node.left and not node.right:  # 到达叶子节点，说明这是一条完整路径，可以处理并返回
            strPath = '->'.join(map(str, path)) # map：“批量处理每个元素”，不需要写 for 循环，此处将所有元素转成字符串
            result.append(strPath)
            return
        
        if node.left:  # 左
            self.dfs(node.left, path, result)
            path.pop()  # 回溯：把刚才添加的 left 节点值移除
        if node.right:  # 右
            self.dfs(node.right, path, result)
            path.pop()  # 回溯：把刚才添加的 right 节点值移除

    
    
if __name__ == "__main__":
    node5 = TreeNode(5)
    node2 = TreeNode(2, None, node5)
    node3 = TreeNode(3)
    root = TreeNode(1, node2, node3)

    solution = Solution()
    paths = solution.binaryTreePaths(root)
    print("所有从根到叶子的路径：")
    for path in paths:
        print(path)
