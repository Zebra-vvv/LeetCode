from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 一句话总结：通过构造虚拟头结点并使用指针操作，成对交换链表中相邻的节点。
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
            tmp1.next = tmp2

            cur = cur.next.next  # cur向后移动两位，继续下一轮交换

        return dummyHead.next


if __name__ == "__main__":

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    solution = Solution()
    newHead = solution.swapPairs(head)
    
    while newHead:
        print(newHead.val)
        newHead = newHead.next