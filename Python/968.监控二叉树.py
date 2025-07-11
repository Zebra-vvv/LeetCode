class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 一句话总结：大体思路就是从低到上，先给叶子节点父节点放个摄像头，然后隔两个节点放一个摄像头，直至到二叉树头结点。
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.result = 0

        # 如果最后根节点未被覆盖，那么一定还需要添加一个摄像头
        if self.dfs(root) == 0:
            self.result += 1
        return self.result

    # 后续遍历
    def dfs(self, node) -> int:

        # 定义三种节点状态：
        # 0：未被摄像头范围覆盖
        # 1：安装有摄像头
        # 2：被摄像头范围覆盖

        if not node:
            return 2
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        if left == 2 and right == 2:
            return 0

        if left == 0 or right == 0:
            self.result += 1
            return 1

        if left == 1 or right == 1:
            return 2

        return -1


if __name__ == "__main__":

    root = TreeNode(0)
    root.left = TreeNode(0)
    root.left.right = TreeNode(0)
    root.left.right.left = TreeNode(0)

    solution = Solution()
    res = solution.minCameraCover(root)  
    print(res)
