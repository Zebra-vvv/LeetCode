class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head:ListNode) -> ListNode:
        slow, fast = head, head

        while fast and fast.next: # 这里不能用fast.next.next, 可能会访问到None.next
            slow = slow.next
            fast = fast.next.next

            # 如果相遇, 表示链表中有环
            if slow == fast:
                index = slow # index是环中相遇点
                
                # 记住数学结论: head到环的入口距离 = index到环的入口的距离
                while head != index:
                    head = head.next
                    index = index.next
                return index
        return None
        
if __name__ == "__main__":
    # 创建链表节点
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    # 构造环
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # 这里构造一个环, 记住next要指向节点本身而不是节点的val
    
    solution = Solution()
    result = solution.detectCycle(node1)
    print(result.val)

