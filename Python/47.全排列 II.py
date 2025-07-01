from typing import List


# 一句话总结：和力扣46题的区别就是，这道题nums可以有重复元素，需要排序数组然后去重，重点注意not self.used[i-1]这个条件
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.path = []
        self.result = []
        self.used = [False] * len(nums)
        nums.sort()
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

            # not self.used[i-1]: 表示只针对树层去重，self.used[i-1]=0，说明上一位没取，那肯定是树层
            if i > 0 and nums[i] == nums[i - 1] and not self.used[i-1]:
                continue

            self.path.append(nums[i])
            self.used[i] = True
            self.backtracking(nums)
            self.used[i] = False
            self.path.pop()


if __name__ == "__main__":
    nums = [1, 1, 2]
    solution = Solution()
    res = solution.permuteUnique(nums)
    print(res)
