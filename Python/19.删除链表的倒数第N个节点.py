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

