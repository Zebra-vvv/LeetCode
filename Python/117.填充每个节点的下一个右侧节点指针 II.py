from typing import List
from collections import deque

class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next  

# 和116题的代码一模一样
class Solution:
    def connect(self, root:'Node') -> 'Node': 
        if not root:
            return root
        que = deque([root])
        while que:
            pre = None
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                if pre:
                    pre.next = node
                pre = node
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return root
    
if __name__ == "__main__":
    # 构建树结构
    node4 = Node(4)
    node5 = Node(5)
    node7 = Node(7)
    node2 = Node(2, node4, node5)
    node3 = Node(3, None, node7)
    root = Node(1, node2, node3)

    # 调用连接方法
    solution = Solution()
    connected_root = solution.connect(root)

    # 打印每层的 next 链表
    def print_next_per_level(start_node):
        while start_node:
            cur = start_node
            while cur:
                print(cur.val, end=" -> ")
                cur = cur.next
            print("None")
            # 移动到下一层最左侧节点
            if start_node.left:
                start_node = start_node.left
            elif start_node.right:
                start_node = start_node.right
            else:
                # 往 next 找下一层起点
                temp = start_node.next
                while temp and not (temp.left or temp.right):
                    temp = temp.next
                start_node = temp.left if temp and temp.left else (temp.right if temp else None)

    print_next_per_level(connected_root)

    
