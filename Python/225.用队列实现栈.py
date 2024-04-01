from collections import deque


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
            # 循环将队列中的第一个元素移到队列的末尾。这个操作相当于将队列中最先进入的元素移到了最后，实现了栈的先进后出（FILO）的特性
            self.que.append(self.que.popleft())
        return self.que.popleft()

    def top(self) -> int:
        if self.empty():
            return None
        return self.que[-1]  # 返回队列中最后一个元素，因为 Python 的负索引表示从后往前数

    def empty(self) -> bool:
        return not self.que


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
