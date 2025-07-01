from typing import List


# 一句话总结：回溯解决组合问题的模板，但是要注意可以重复选取元素，startIndex传i
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.path = []
        self.result = []
        self.backtracking(candidates, target, curSum=0, startIndex=0)
        return self.result

    # 对于组合问题：
    # 如果是一个集合来求组合的话，就需要startIndex
    # 如果是多个集合取组合，各个集合之间相互不影响，那么就不用startIndex
    def backtracking(self, candidates, target, curSum, startIndex):

        # 剪枝
        if curSum > target:
            return

        # 终止条件
        if curSum == target:
            self.result.append(self.path[:])

        # 单层递归逻辑
        for i in range(startIndex, len(candidates)):
            self.path.append(candidates[i])
            curSum += candidates[i]

            # 可以重复选取元素，startIndex传i
            self.backtracking(candidates, target, curSum, i)
            curSum -= candidates[i]
            self.path.pop()


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    solution = Solution()
    res = solution.combinationSum(candidates, target)
    print(res)
