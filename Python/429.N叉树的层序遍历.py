from typing import List
from collections import deque

class Node:
    def __init__(self, val:int = None, children:List['Node'] = None):
        self.val = val
        self.children = children if children is not None else [] # 健壮性

# 一句话总结：和二叉树层序遍历差不多，只不过需要for循环来加入一个节点的所有孩子
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        que = deque([root])
        result = []
        
        while que:
            level = []
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                level.append(node.val)

                # for循环加入当前节点的所有孩子
                for child in node.children:
                    que.append(child)

            result.append(level)
        return result

if __name__ == "__main__":
    # 构造如下 N 叉树：
    #         1
    #      /  |  \
    #     2   3   4
    #        / \
    #       5   6
    node5 = Node(5)
    node6 = Node(6)
    node2 = Node(2)
    node3 = Node(3, [node5, node6])
    node4 = Node(4)
    root = Node(1, [node2, node3, node4])

    solution = Solution()
    res = solution.levelOrder(root)
    print(res)  # 输出：[[1], [2, 3, 4], [5, 6]]