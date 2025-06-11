from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

# 一句话总结：利用快指针先走 n 步，然后快慢指针一起走，当快指针到达末尾时，慢指针刚好在待删除节点的前一个位置。这样就能在单次遍历中删除倒数第 n 个节点。
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