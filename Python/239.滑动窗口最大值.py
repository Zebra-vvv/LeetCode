from collections import deque
from typing import List

# 自定义一个从大到小的单调队列
class Myqueue:
    def __init__(self):
        self.queue = deque()

    def push(self, value):
        
        # 如果value比前面的值都大, 就持续抛弃前面的值, 因为较小值没有必要维护
        while self.queue and self.queue[-1] < value:
            self.queue.pop()
        self.queue.append(value)

    def pop(self, value):
        # 当前遍历值等于单调栈最左侧（队头，最大值）的值，说明当前元素真的需要手动pop掉(较小值在较大值push时就会被抛弃)
        if self.queue and self.queue[0] == value:
            self.queue.popleft()

    def getMaxValue(self):
        return self.queue[0] # 最左侧的元素（队头）

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        myqueue = Myqueue()
        result = []

        # 先将前k个元素放入单调栈中
        for i in range(k):
            myqueue.push(nums[i])
        # 记录第一个滑动窗口的最大值
        result.append(myqueue.getMaxValue())

        # 开始移动滑动窗口
        for i in range(k, len(nums)):
            myqueue.pop(nums[i - k])  # 弹出窗口最左侧的那个元素（可能早就弹出了）
            myqueue.push(nums[i])  # 将当前元素加入单调队列
            result.append(myqueue.getMaxValue())  # 记录当前窗口内的最大值
        return result

if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    solution = Solution()
    result = solution.maxSlidingWindow(nums, k)
    print(result)
