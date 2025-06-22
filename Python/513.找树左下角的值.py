from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 用层序遍历模板最简单，递归法反而复杂
# 一句话总结：res 会在每一层都被更新为该层最左节点的值，最终留下的就是最后一层最左节点的值。
class Solution:
    def findBottomLeftValue(self, root:TreeNode) -> int:
        if not root:
            return []

        queue = deque([root]) # TreeNode 是个普通类，不是可迭代对象，要用列表包一层。
        result = 0 # 存放最终结果
        
        # 总之就是pop一个节点的同时，加入它的左右孩子
        while queue:
            
            size = len(queue) # 每层的节点数

            # for循环执行1次，收集一个节点；整个for循环结束之后，收集一层节点
            for i in range(size):
                node = queue.popleft()
                
                # 这一层的第一个节点
                if i == 0:
                    result = node.val # 更新

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
    result = solution.findBottomLeftValue(node1)
    print(result)