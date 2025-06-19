from collections import deque

# 一句话总结：
# 用一个单向队列 que 模拟栈，为了实现 pop() 弹出“最后入栈的元素”，我们要把前面所有元素“让一让”，让最后那个排到前面来，再弹出它。
class MyStack:
    
    def __init__(self):
        self.que = deque() # 虽然deque是双端队列，但是这题只当成了一个单向队列来用

    def push(self, x: int) -> None:
        self.que.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        for i in range(len(self.que)-1):
            # 在 Python 的 collections.deque 中，默认的append是右边进入，popleft顾名思义是从左边弹出
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
