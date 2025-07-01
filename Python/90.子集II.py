from typing import List


# 一句话总结：和力扣78题的区别就是这道题，给出的nums里面可能有重复元素，需要树层去重
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.path = []
        self.result = []

        # 树层去重，需要先排序
        nums.sort()

        self.backtracking(nums, startIndex=0)
        return self.result

    def backtracking(self, nums, startIndex):

        self.result.append(self.path[:])

        for i in range(startIndex, len(nums)):

            # i > startIndex：确保只对树层去重，对树枝不去重
            # 因为只有横向for循环导致i自增的时候，才会出现 i > startIndex
            if i > startIndex and nums[i] == nums[i-1]:
                continue

            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()


if __name__ == "__main__":
    nums = [1, 2, 2]
    solution = Solution()
    res = solution.subsetsWithDup(nums)
    print(res)
