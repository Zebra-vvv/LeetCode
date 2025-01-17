class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.dummyHead = ListNode()  # 虚拟头结点
        self.size = 0               # 链表长度

    def get(self, index: int) -> int:

        if index < 0 or index >= self.size:  # 注意这里有等号, 因为只能取已有节点的值
            return -1

        current = self.dummyHead.next
        for i in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        self.dummyHead.next = ListNode(val, self.dummyHead.next)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        current = self.dummyHead
        while current.next:
            current = current.next
        current.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:

        if index < 0 or index > self.size:  # 这里没有等号, 因为取等号代表在链尾插入, 是合法情况
            return

        current = self.dummyHead
        for i in range(index):
            current = current.next
        current.next = ListNode(val, current.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:

        if index < 0 or index >= self.size:  # 注意这里有等号, 因为只能删已有节点
            return

        current = self.dummyHead
        for i in range(index):
            current = current.next
        current.next = current.next.next
        self.size -= 1


if __name__ == "__main__":
    # 创建一个链表对象
    linkedList = MyLinkedList()

    # 在头部添加节点
    linkedList.addAtHead(1)
    linkedList.addAtHead(2)
    linkedList.addAtHead(3)

    # 在尾部添加节点
    linkedList.addAtTail(4)
    linkedList.addAtTail(5)

    # 打印链表当前状态
    print("Linked List after additions:")
    current = linkedList.dummyHead.next
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

    # 获取指定位置的节点值
    print("Value at index 2:", linkedList.get(2))

    # 在指定位置添加节点
    linkedList.addAtIndex(2, 10)
    print("Linked List after adding at index 2:")
    current = linkedList.dummyHead.next
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

    # 删除指定位置的节点
    linkedList.deleteAtIndex(3)
    print("Linked List after deleting at index 3:")
    current = linkedList.dummyHead.next
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
