from typing import List

# 一句话总结：
# 本题数组candidates的元素是有重复的，而 39.组合总和 是无重复元素的数组candidates，所以需要在横向树层上去重
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.path = []
        self.result = []

        # ✅ 排序是去重的前提
        candidates.sort()

        self.backtracking(candidates, target, curSum=0, startIndex=0)
        return self.result

    def backtracking(self, candidates, target, curSum, startIndex):

        # 剪枝
        if curSum > target:
            return

        # 终止条件
        if curSum == target:
            self.result.append(self.path[:])
            return 

        # 单层递归逻辑
        for i in range(startIndex, len(candidates)):
            
            # i > startIndex：允许不同层使用相同的数
            # candidates[i] == candidates[i - 1]：跳过相邻重复值
            if i > startIndex and candidates[i] == candidates[i - 1]:
                continue  

            self.path.append(candidates[i])
            curSum += candidates[i]
            self.backtracking(candidates, target, curSum, i+1)
            curSum -= candidates[i]
            self.path.pop()


if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    solution = Solution()
    res = solution.combinationSum2(candidates, target)
    print(res)
