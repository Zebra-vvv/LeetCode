class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def getIntersectionNode(self, headA:ListNode, headB:ListNode) -> ListNode:

        # 计算两个链表长度
        cur = headA
        sizeA = 0
        while cur:
            cur = cur.next
            sizeA += 1
        cur = headB
        sizeB = 0
        while cur:
            cur = cur.next
            sizeB += 1

        # 对齐两个链表的起点
        curA = headA
        curB = headB
        if sizeA > sizeB:
            for i in range(sizeA-sizeB):
                curA = curA.next
        else:
            for i in range(sizeB-sizeA):
                curB = curB.next
        
        # 找到相交节点
        while curA:
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next
        return None

if __name__ == "__main__":
    common_node = ListNode(8,ListNode(4,ListNode(5)))
    headA = ListNode(4,ListNode(1,common_node))
    headB = ListNode(5,ListNode(0,ListNode(1,common_node)))

    solution = Solution()
    result = solution.getIntersectionNode(headA, headB)
    print(result.val)
        