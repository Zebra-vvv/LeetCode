from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        dis = self.getLength(headA) - self.getLength(headB)
        
        # 通过移动较长的链表，使两链表长度相等
        if dis > 0:
            headA = self.moveForward(headA, dis)
        else:
            headB = self.moveForward(headB, abs(dis))
        
        # 将两个头向前移动，直到它们相交
        while headA:
            if headA == headB: # 需要判断的是节点本身，而不是节点的值
                return headA
            headA = headA.next
            headB = headB.next
        
        return None
    
    def getLength(self, head: ListNode) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    
    def moveForward(self, head: ListNode, steps: int) -> ListNode:
        while steps > 0:
            head = head.next
            steps -= 1
        return head


if __name__ == "__main__":
    # 创建一些链表节点
    common_node = ListNode(8, ListNode(4, ListNode(5)))

    headA = ListNode(4, ListNode(1, common_node))
    headB = ListNode(5, ListNode(6, ListNode(1, common_node)))

    # 创建 Solution 实例
    solution = Solution()

    # 调用 getIntersectionNode 方法
    intersection_node = solution.getIntersectionNode(headA, headB)

    if intersection_node:
        print(f"Intersection Node Value: {intersection_node.val}")
    else:
        print("No intersection node found.")
