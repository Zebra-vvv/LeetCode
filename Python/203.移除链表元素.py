from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Optional 是 Python 中的类型提示（Type Hints）中的一个类型，它表示一个值可以是特定类型，也可以是 None
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # 构建一个虚拟头结点
        dummyNode = ListNode()
        dummyNode.next = head
        cur = dummyNode

        while cur.next != None:  # 始终判断的是 cur.next 的值, 这个值才能被比较然后删除
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummyNode.next
    
def printLinkedList(head: Optional[ListNode]):
    # 辅助函数，用于打印链表
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

if __name__ == "__main__":
    # 创建测试链表：1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
    test_head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    
    # 打印原始链表
    print("原始链表：")
    printLinkedList(test_head)
    
    # 创建 Solution 类的实例
    solution = Solution()
    
    # 调用 removeElements 方法，删除值为 6 的节点
    result_head = solution.removeElements(test_head, 6)
    
    # 打印删除节点后的链表
    print("\n删除值为 6 的节点后的链表：")
    printLinkedList(result_head)


