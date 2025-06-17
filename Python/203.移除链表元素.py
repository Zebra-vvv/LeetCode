from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 一句话总结：使用虚拟头结点，遍历链表并删除所有值等于给定值的节点，注意删除后指针不前移以确保不跳过节点。
class Solution:
    def removeElements(self, head:ListNode, val:int) -> ListNode:

        # 构建一个虚拟头结点
        dummyNode = ListNode()
        dummyNode.next = head
        cur = dummyNode

        while cur.next != None:  # 始终判断的是 cur.next 的值, 这个值才能被比较然后删除
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next # 注意这句必须放在else里面，因为删除之后，cur.next就已经指向下一个节点了

        return dummyNode.next


# 辅助函数，用于打印链表 
def printLinkedList(head: Optional[ListNode]):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


if __name__ == "__main__":
    # 创建测试链表：1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
    test_head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    
    print("原始链表：")
    printLinkedList(test_head)

    solution = Solution()
    result_head = solution.removeElements(test_head, 6)
    
    print("\n删除值为 6 的节点后的链表：")
    printLinkedList(result_head)


