from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyHead=ListNode(next=head)
        fast,slow=dummyHead,dummyHead
        
        # fast指针要比slow先走n+1步, 这样才能让slow停留在要删除的节点前一个
        for i in range(n+1):
            fast=fast.next
        
        while fast:
            fast=fast.next
            slow=slow.next
        
        # 删除倒数第n个节点
        slow.next=slow.next.next
        
        return dummyHead.next

if __name__ == "__main__":
    # 创建一个链表: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    # 打印原始链表
    print("Original Linked List:")
    cur = head
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("None")

    # 创建 Solution 实例
    solution = Solution()

    # 删除倒数第2个节点
    n = 2
    new_head = solution.removeNthFromEnd(head, n)

    # 打印删除后的链表
    print(f"\nLinked List after removing {n}th node from the end:")
    cur = new_head
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("None")
