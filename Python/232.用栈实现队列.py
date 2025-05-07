class MyQueue:

    def __init__(self):
        # python的栈可以用List来实现，Python的List提供了足够的方法来模拟栈的所有操作
        self.stack_in = []  # 用于接收 push 进来的数据（原始顺序）
        self.stack_out = [] # 用于执行 pop/peek，保存反转后的顺序

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        if self.stack_out:
            return self.stack_out.pop() # 这里调用的都是List的pop方法，而不是自身
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self) -> int:
        # 复用pop的代码, 只要再append回去就行
        ans = self.pop()  # 调用的是MyQueue类的pop
        self.stack_out.append(ans)
        return ans

    def empty(self) -> bool:
        return len(self.stack_in) == 0 and len(self.stack_out) == 0


if __name__ == "__main__":
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    print(obj.pop())
    print(obj.peek())
    obj.pop()
    obj.pop()
    print(obj.empty())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
