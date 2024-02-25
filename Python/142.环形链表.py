from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                index = slow

                while index != head: # 直接在while中判断，不会漏判
                    index = index.next
                    head = head.next
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
    node4.next = node2  # 这里构造一个环

    solution = Solution()
    result = solution.detectCycle(node1)

    if result:
        print(f"链表中存在环，入口点的值为 {result.val}")
    else:
        print("链表中不存在环")
