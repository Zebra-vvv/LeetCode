from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

class Solution:
    def removeNthFromEnd(self, head:ListNode, n:int) -> ListNode:
        dummyHead = ListNode()
        dummyHead.next = head
        
        fast, slow = dummyHead, dummyHead
        for i in range(n):
            fast = fast.next
        while fast.next: # 这里要判断fast.next, 纸笔模拟就知道了, 这样slow停下的位置正好
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummyHead.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3) 
    head.next.next.next = ListNode(4)
    head.next.next.next.next  = ListNode(5)

    solution = Solution()
    head = solution.removeNthFromEnd(head, 2)

    while head:
        print(head.val)
        head = head.next