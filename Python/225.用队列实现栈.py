from collections import deque

#队列是先进先出（FIFO），栈是后进先出（LIFO）。
#我们用一个队列 que 模拟栈，为了实现 pop() 弹出“最后入栈的元素”，我们要把前面所有元素“让一让”，让最后那个排到前面来，再弹出它。
class MyStack:
    # 一个队列在模拟栈弹出元素的时候只要将队列头部的元素（除了最后一个元素外） 重新添加到队列尾部，此时再去弹出元素就是栈的顺序了。
    def __init__(self):
        self.que = deque()

    def push(self, x: int) -> None:
        self.que.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        for i in range(len(self.que)-1):
            # 在 Python 的 collections.deque 中，队列默认的“入口”是右边，出口是左边
            # 循环将队列中的第一个元素移到队列的末尾。这个操作相当于将队列中最先进入的元素移到了最后，实现了栈的先进后出（FILO）的特性
            self.que.append(self.que.popleft())
        return self.que.popleft()

    def top(self) -> int:
        if self.empty():
            return None
        return self.que[-1]  # 返回队列中最后一个元素，因为 Python 的负索引表示从后往前数

    def empty(self) -> bool:
        return len(self.que) == 0 


if __name__ == "__main__":
    obj = MyStack()
    a, b, c = 1, 2, 3
    obj.push(a)
    obj.push(b)
    obj.push(c)
    param_1 = obj.pop()
    param_2 = obj.top()
    param_3 = obj.empty()
    print(param_1)
    print(param_2)
    print(param_3)
