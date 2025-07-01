from typing import List


# 一句话总结：排列问题和组合问题不同，不需要startIndex，而是需要一个全局变量used数组标记已经使用过的元素
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.path = []
        self.result = []

        # 全局变量
        self.used = [False] * len(nums)

        self.backtracking(nums)
        return self.result

    def backtracking(self, nums):

        # 终止条件
        if len(self.path) == len(nums):
            self.result.append(self.path[:])
            return

        # 单层递归逻辑
        for i in range(len(nums)):
            
            # 跳过已经使用过的元素
            if self.used[i]:
                continue

            self.path.append(nums[i])
            self.used[i] = True
            self.backtracking(nums)
            self.used[i] = False
            self.path.pop()


if __name__ == "__main__":
    nums = [1, 2, 3]
    solution = Solution()
    res = solution.permute(nums)
    print(res)
