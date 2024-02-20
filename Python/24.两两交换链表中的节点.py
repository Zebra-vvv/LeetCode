from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(next=head)
        cur = dummyHead

        while cur.next and cur.next.next:
            tmp1 = cur.next
            tmp2 = cur.next.next.next

            # 画图理解以下三步
            cur.next = cur.next.next
            cur.next.next = tmp1
            cur.next.next.next = tmp2

            cur = cur.next.next  # cur向后移动两位，继续下一轮交换

        return dummyHead.next


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

    # 调用 swapPairs 方法交换相邻节点
    swapped_head = solution.swapPairs(head)

    # 打印交换后的链表
    print("\n相邻节点交换后的链表:")
    current = swapped_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
