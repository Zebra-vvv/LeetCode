from collections import deque
from typing import List

# 自定义一个从大到小的单调队列
class Myqueue:
    def __init__(self):
        self.queue = deque()

    def pop(self, value):
        # 当前遍历值等于单调栈最左侧的值（最大值），说明当前元素真的需要被pop掉
        if self.queue and self.queue[0] == value:
            self.queue.popleft()

    def push(self, value):
        while self.queue and self.queue[-1] < value:
            self.queue.pop()
        self.queue.append(value)

    def getMaxValue(self):
        return self.queue[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        myqueue = Myqueue()
        result = []

        # 先将前k个元素放入单调栈中
        for i in range(k):
            myqueue.push(nums[i])
        # 先记录前k个元素的最大值
        result.append(myqueue.getMaxValue())

        # 遍历k个之后的元素
        for i in range(k, len(nums)):
            myqueue.pop(nums[i - k])  # 移除窗口最左侧的元素
            myqueue.push(nums[i])  # 将当前元素加入单调队列
            result.append(myqueue.getMaxValue())  # 记录当前窗口内的最大值
        return result

if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    solution = Solution()
    result = solution.maxSlidingWindow(nums, k)
    print(result)
