from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 双指针法
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            tmp = cur.next  # 先把cur.next保存下来
            cur.next = pre

            # 移动cur和pre指针
            pre = cur
            cur = tmp
        return pre


if __name__ == "__main__":
    # 创建链表: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # 打印原始链表
    print("原始链表:")
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

    # 创建 Solution 类的实例
    solution = Solution()

    # 调用 reverseList 方法反转链表
    reversed_head = solution.reverseList(head)

    # 打印反转后的链表
    print("\n反转后的链表:")
    current = reversed_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
