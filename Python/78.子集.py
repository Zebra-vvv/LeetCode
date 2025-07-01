from typing import List


# 一句话总结：回溯的标准模板，没有终止条件，每次进入递归，都直接收集结果
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.path = []
        self.result = []
        self.backtracking(nums, startIndex=0)
        return self.result

    def backtracking(self, nums, startIndex):

        # 本题可以不写递归终止条件，因为要收获所有节点（组合问题是收获叶子结点）
        self.result.append(self.path[:])

        # 单层递归逻辑
        for i in range(startIndex, len(nums)):
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()


if __name__ == "__main__":
    nums = [1, 2, 3]
    solution = Solution()
    res = solution.subsets(nums)
    print(res)
